---
name: h3xn-onlyno999
description: H3XN 武打短剧生产 Agent（XN＝西瓜＋动作导演的新线）：西瓜短剧 Agent 前半截（剧本/分镜流水线）＋ fight-prompt-director 动作导演（打斗提示词编排）＋ RunningHub 武打设计专用云端工作流 2110403291422220289 出片的独立技能包。第一次安装先分别拉取两个上游组件（各自独立、各自在线更新），出片只认本包出口。与 H3XG-onlyno999（出口 2110385615559806978）是两条线、背后的 API 模型不一样，严禁混用。用户说「H3XN」「/H3XN-onlyno999」「用 H3XN 出片」时触发。
---

# H3XN-onlyno999 · 武打短剧生产 Agent

## Purpose
一句话故事进，一条云端生成的武打短剧成片出。结构是「西瓜前半截 ＋ 动作导演编词 ＋ 武打专用出口」：
- **剧本 / 分镜 / 提示词流水线**：西瓜短剧 Agent（xigua-drama-agent）负责事件图谱、抽角色/场景/道具、分镜拆解与审查。
- **动作戏编排**：凡打斗、追逐、对抗、演武段落，提示词一律过 `fight-prompt-director` 技能（动作导演）编排——动作因果链、空间方向、镜头职责、跨镜连续、速度轴（标准/极速）与强度方案，都按那本技能执行，本包不另发明动作词法。
- **出片**：只走云端 RunningHub 工作流 `2110403291422220289`（用户自搭的武打设计专用出口）。不用本地 ComfyUI 出片，不用宿主原生视频生成顶替，更不许借用其他线的出口。

本包**独立自含**：派发脚本、节点图谱都在本目录内；两个上游组件各是独立仓库、各连各自上游在线更新，本包不 vendoring 它们的代码、也不改它们。

## 第一次安装（First Install）
1. 拉西瓜短剧 Agent 本体（独立克隆、在线更新）：
   ```bash
   git clone https://github.com/zjs134679-sketch/xigua-drama-agent.git ~/workspace/xigua-drama-agent
   cd ~/workspace/xigua-drama-agent/backend && python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
   backend/.venv/bin/python scripts/_gen_art_styles.py   # 生成 11 个 xg_* 画风包（仓库不带）
   cd ../frontend && npm install && npm run build
   ```
   后端启动：`backend/.venv/bin/python -m uvicorn app.main:app --host 127.0.0.1 --port 5678`（健康检查 GET /health 200、108 个接口）。已知基线：西瓜自带测试有个别失败源于仓库未附带的运行时配置，非安装故障，不为此停工。
2. 拉动作导演技能（独立技能版、在线更新）：把 `https://github.com/irenerachel/fight-prompt-director.git` 克隆到宿主的技能目录（本机：`~/workspace/skills/fight-prompt-director/`，目录本尊即 git 克隆，更新时在目录内 `git pull`）。
3. 云端工作流激活（一次性）：工作流 `2110403291422220289` 若探针返回 **810**，须先在 RunningHub 网页打开并**运行一次**激活（之后回 803 即可派发）。激活是账号侧动作，Agent 只探针确认状态，不代跑。

## Tooling
- 西瓜本体：`~/workspace/xigua-drama-agent`（FastAPI :5678＋React 前端；本 Agent 只用其前半截流水线，不用它的本地 ComfyUI 算力）。
- 动作导演：技能 `fight-prompt-director`（本机 `~/workspace/skills/fight-prompt-director/`）。
- 云端出口：RunningHub **workflow** `2110403291422220289`（武打设计专用），端点 `POST /openapi/v2/run/workflow/2110403291422220289`，Standard 实例（`instanceType=default`）。**不是** H3XG 的 2110385615559806978——两条线背后的 API 模型不一样，节点图谱也完全不同（本流 29 节点全在 115–179），严禁互切、混用。
- 派发：`bin/dispatch_wf.py`（参数化：提示词文件/时长/画幅/种子/图槽/可选音频/输出目录；含上传、轮询与下载，results URL 约 24h 有效、SUCCESS 后立即下载）。
- 探针：`bin/probe_step1.py`（零扣费查激活状态：810 未激活 / 803 已激活）；节点普查 `bin/census_nodes.py`（bogus 字段哨兵法，全程零建任务零扣费）。
- 节点图谱：`references/node_map.md`（2026-10-15 普查定版，29 节点＋定向字段验证＋待首派验证项）。
- 鉴权：RunningHub 走 surrogate 凭据 `custom.runninghub`（dynamic_credentials helper），脚本内已封装，Key 不落盘、不进包。
- 交付盘：Google Drive「成片」文件夹（hatch_gws_cli drive +upload）。

## 云端派发口（普查定版）
| 用途 | 节点.字段 |
| :--- | :--- |
| 提示词（文本原语） | 138.value |
| 提示词（主生成节点直入口） | 136.prompt（与 138 双入口并存，派发器默认两处同填，首派回片后定版） |
| 时长（秒） | 132.value |
| 画幅 | 115.aspect_ratio（如 `9:16 (Portrait Widescreen)`) |
| 种子 | 129.noise_seed |
| 参考图（4 槽） | 137 / 139 / 167 / 173.image |
| 音频入口（输出合成节点） | 148.audio（语义待首派验证，无音频需求先不挂） |

槽位惯例：**主角三视图卡原图 → Node 137**；场景图 → Node 139；167/173 备用（第二主体/道具/构图参考）。本流只有 4 个图槽，没有 H3XG 那种 9 图槽，也没有三路音频——其他线的静音等口径**不移植**到本线。

## Workflow
1. **接单**：听完用户的一句话故事/剧本要求；定主角与时长、画幅（默认 9:16 竖屏）。
2. **备图**：人物三视图用现成卡原图直用、不重绘不裁切；场景图等缺图由 Agent 本地绘制（纯场景、无人物、画幅与成片一致），画完自检再用。
3. **写提示词**：
   - 剧本与分镜走西瓜前半截流水线产出。
   - 动作段：过 `fight-prompt-director` 编排（每轮交锋写全因果链：发起→接触→回应→位移→下一拍接口；角色各自的优势距离与反制策略；镜头职责与轴线写死）。速度与强度按用户当次点名选轴，未点名先按该技能的规矩补问一次速度档。
   - 打斗节奏铁律（用户定版）：速度写进提示词成为角色动作本身的迅猛节奏，全程高速一气呵成，绝无慢动作/定格/停顿；不许后期变速凑时长。
   - 角色长相只许引用参考图，不许用文字复述五官；签名造型逐项写死。
4. **派发前探针**：`bin/probe_step1.py` 确认 803；810 就停下报用户去网页运行一次，不许换出口顶替。
5. **派发**：`bin/dispatch_wf.py`——提示词同填 138.value 与 136.prompt；Standard 实例；记任务号。
6. **取回**：轮询到 SUCCESS 立即下载原片（原生尺寸交付，不裁不缩）。
7. **质检门**（自己跑完）：抽帧查脸对卡/造型/场景 1:1/无烧字水印；动作段逐拍核因果链有没有拍出来（漏拍、软打、慢镜都是病）；有对白时 ASR 核台词内容与次数；音频只许原生对白＋现场拟音，检出配乐/旁白＝污染；规格核时长/分辨率/帧率。
8. **交付**：转码收尾（H.264 High@L4.0、yuv420p、bt709、AAC LC 48kHz、剥元数据、+faststart、尺寸保持云端原生）→ 聊天附件＋Drive「成片」夹链接。

## 铁律
1. 出片只许走 `2110403291422220289`；不许切去 H3XG 的 2110385615559806978 或任何其他出口——每个出口背后的 API 模型不一样。
2. 两个上游组件保持独立：西瓜本体与 fight-prompt-director 各自是独立克隆、各自在线更新，本包不改它们、不把它们并进本包仓库。
3. 每派必先免费探针；探针不过（810）就停，不许先派再说。
4. 动作段提示词必须过 fight-prompt-director 编排，不许手写简化版应付。
5. 三视图现成图只直用、不动图；缺什么图补画什么图。
6. 提示词双入口（138/136）的生效结论以首派回片为准，回片后回写 `references/node_map.md` 定版，在此之前不许宣称已定版。
7. 质检不过自己修/重派；只有超预算或修不好才上报用户。
