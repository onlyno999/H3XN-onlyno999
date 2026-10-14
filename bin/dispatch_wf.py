#!/usr/bin/env python3
"""H3XN dispatcher - RunningHub workflow 2110403291422220289 (fight-design line).

H3XN-onlyno999 cloud exit. Standalone line, NOT part of H3XG (whose exit is 2110385615559806978).
Node map: see references/node_map.md in this package.
Prompt is written to BOTH 138.value and 136.prompt (dual entry, to be
pinned down after the first real dispatch).

Usage:
  python3 dispatch_fight_wf.py --probe
  python3 dispatch_fight_wf.py --prompt-file P.txt --duration 5 \
      --image 137=card.png --image 139=scene.png --out-dir ./prod
"""
import sys, os, json, time, argparse, mimetypes, urllib.request
sys.path.insert(0, "/opt/hatch/skills/skill-creator/bin")
from dynamic_credentials import add_surrogate_to_request

BASE = "https://www.runninghub.cn"
WF = "2110403291422220289"
CRED = "custom.runninghub"
UA = "h3xn-dispatch/1.0"

def post_json(path, payload, timeout=60):
    req = urllib.request.Request(BASE + path, data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json", "User-Agent": UA}, method="POST")
    add_surrogate_to_request(req, CRED, allowed_hosts=["www.runninghub.cn"])
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8"))

def check(resp, ctx):
    ec = resp.get("errorCode")
    if ec not in (None, "", 0, "0"):
        raise SystemExit(f"[{ctx}] errorCode={ec} errorMessage={resp.get('errorMessage')}")
    return resp

def probe():
    payload = {"nodeInfoList": [{"nodeId": "99999", "fieldName": "__bogus_probe_field__", "fieldValue": "x"}]}
    r = post_json(f"/openapi/v2/run/workflow/{WF}", payload, timeout=30)
    print(f"probe errorCode={r.get('errorCode')} (803=active, 810=needs a web run first)")
    return 0 if str(r.get("errorCode")) == "803" else 1

def upload_media(path):
    path = os.path.expanduser(path)
    with open(path, "rb") as f: data = f.read()
    boundary = "----fightwf" + os.urandom(8).hex()
    fname = os.path.basename(path)
    ctype = mimetypes.guess_type(fname)[0] or "application/octet-stream"
    body = (f"--{boundary}\r\n"
            f'Content-Disposition: form-data; name="file"; filename="{fname}"\r\n'
            f"Content-Type: {ctype}\r\n\r\n").encode() + data + f"\r\n--{boundary}--\r\n".encode()
    req = urllib.request.Request(BASE + "/openapi/v2/media/upload/binary", data=body,
        headers={"Content-Type": f"multipart/form-data; boundary={boundary}", "User-Agent": UA}, method="POST")
    add_surrogate_to_request(req, CRED, allowed_hosts=["www.runninghub.cn"])
    with urllib.request.urlopen(req, timeout=120) as resp:
        r = json.loads(resp.read().decode("utf-8"))
    check(r, "upload")
    fn = (r.get("data") or {}).get("fileName")
    if not fn: raise SystemExit(f"upload no fileName: {json.dumps(r)[:300]}")
    print(f"[+] uploaded {path} -> {fn} ({len(data)//1024}KB)", flush=True)
    return fn

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--probe", action="store_true")
    ap.add_argument("--prompt-file", default="")
    ap.add_argument("--duration", type=float, default=5)
    ap.add_argument("--aspect", default="9:16 (Portrait Widescreen)")
    ap.add_argument("--seed", type=int, default=20261015)
    ap.add_argument("--image", action="append", default=[], help="NODE=path (137/139/167/173), repeatable")
    ap.add_argument("--audio", default="", help="local audio path -> Node 148.audio")
    ap.add_argument("--no-direct-prompt", action="store_true", help="skip 136.prompt, only 138.value")
    ap.add_argument("--out-dir", default="")
    ap.add_argument("--max-poll", type=int, default=1500)
    a = ap.parse_args()
    if a.probe:
        return probe()
    if not a.prompt_file or not a.out_dir:
        raise SystemExit("need --prompt-file and --out-dir (or --probe)")
    os.makedirs(a.out_dir, exist_ok=True)
    prompt = open(a.prompt_file, encoding="utf-8").read()
    nodes = [
        {"nodeId": "138", "fieldName": "value", "fieldValue": prompt},
        {"nodeId": "132", "fieldName": "value", "fieldValue": a.duration},
        {"nodeId": "115", "fieldName": "aspect_ratio", "fieldValue": a.aspect},
        {"nodeId": "129", "fieldName": "noise_seed", "fieldValue": a.seed},
    ]
    if not a.no_direct_prompt:
        nodes.append({"nodeId": "136", "fieldName": "prompt", "fieldValue": prompt})
    for item in a.image:
        nid, _, path = item.partition("=")
        if nid not in ("137", "139", "167", "173"):
            raise SystemExit(f"image node must be one of 137/139/167/173, got {nid}")
        nodes.append({"nodeId": nid, "fieldName": "image", "fieldValue": upload_media(path)})
    if a.audio:
        nodes.append({"nodeId": "148", "fieldName": "audio", "fieldValue": upload_media(a.audio)})
    r = post_json(f"/openapi/v2/run/workflow/{WF}",
                  {"nodeInfoList": nodes, "instanceType": "default", "usePersonalQueue": False})
    check(r, "dispatch")
    task_id = r.get("taskId")
    print(f"[+] task created: {task_id}", flush=True)
    with open(os.path.join(a.out_dir, "task_id.txt"), "w") as f: f.write(str(task_id))
    deadline = time.time() + a.max_poll
    while time.time() < deadline:
        time.sleep(10)
        q = post_json("/openapi/v2/query", {"taskId": task_id}, timeout=30)
        status = q.get("status")
        print(f"[.] status={status}", flush=True)
        if status in ("SUCCESS", "COMPLETED"):
            with open(os.path.join(a.out_dir, "results.json"), "w") as f:
                json.dump(q, f, ensure_ascii=False, indent=2)
            for item in (q.get("results") or []):
                url = item.get("url")
                if url and (".mp4" in url or item.get("outputType") == "mp4"):
                    dest = os.path.join(a.out_dir, "seg_raw.mp4")
                    req = urllib.request.Request(url, headers={"User-Agent": UA})
                    with urllib.request.urlopen(req, timeout=300) as resp, open(dest, "wb") as out:
                        out.write(resp.read())
                    print(f"[+] downloaded -> {dest}", flush=True)
            return 0
        if status in ("FAILED", "ERROR", "CANCELLED"):
            print(json.dumps(q, ensure_ascii=False)[:800], flush=True)
            raise SystemExit("task failed")
    raise SystemExit("poll timeout")

if __name__ == "__main__":
    sys.exit(main())
