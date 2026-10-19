---
name: h3xn-onlyno999
description: H3XN 武打短剧生产 Agent（XN＝西瓜＋动作导演的新线）：专做动作打斗，由三个组件构成——①西瓜短剧 Agent 前半截（剧本/分镜流水线）② fight-prompt-director 动作导演（打斗提示词编排）③ xuanhuan-combat-director 玄幻仙侠战斗导演（玄幻/仙侠/法术对轰的打戏导演系统）——再挂 RunningHub 武打设计专用云端工作流 2110403291422220289 出片的独立技能包；本文件同时收录刚学入的打戏技法技能索引与本包外部接口（出口/节点/派发口径）全文，一册在手。第一次安装先分别拉取三个上游组件（各自独立、各自在线更新），出片只认本包出口。与 H3XG-onlyno999（出口 2110385615559806978）是两条线、背后的 API 模型不一样，严禁混用。用户说「H3XN」「/H3XN-onlyno999」「用 H3XN 出片」时触发。
---

# H3XN-onlyno999 · 武打短剧生产 Agent

## Purpose
一句话故事进，一条云端生成的武打短剧成片出。本 Agent **专做动作打斗**，由**三个组件**构成，再挂武打专用出口出片：
- **组件一 · 剧本 / 分镜流水线（西瓜）**：西瓜短剧 Agent（xigua-drama-agent）前半截负责事件图谱、抽角色/场景/道具、分镜拆解与审查。
- **组件二 · 动作导演（fight-prompt-director）**：凡打斗、追逐、对抗、演武段落，提示词一律过 `fight-prompt-director` 编排——动作因果链、空间方向、镜头职责、跨镜连续、速度轴（标准/极速）与强度方案，都按那本技能执行，本包不另发明动作词法。
- **组件三 · 玄幻仙侠战斗导演（xuanhuan-combat-director）**：玄幻/仙侠/神魔题材的打戏导演系统（V2.6.0，用户 2026-10-15 令装入并定为本 Agent 第三组件）——三轮攻守骨架、2–3 秒整秒细切（一镜一动一反馈）、瞬发瞬收动词铁律（禁长时状态动词）、终结收束 A/B/C/D 四协议、反杀三段式＋视觉反超、近景机枪对招引擎、13 种复合元素、法阵领域尺度、招式总库与写实/修仙双档参数库。题材是玄幻仙侠/法术对轰/终结技时，动作段以组件三为主导演，组件二管因果链与跨镜连续兜底；写实/日常题材仍以组件二为主。
- **出片**：只走云端 RunningHub 工作流 `2110403291422220289`（用户自搭的武打设计专用出口）。不用本地 ComfyUI 出片，不用宿主原生视频生成顶替，更不许借用其他线的出口。

本包**独立自含**：派发脚本、节点图谱都在本目录内；三个上游组件各是独立仓库、各连各自上游在线更新，本包不 vendoring 它们的代码、也不改它们。本文件末尾另设两节：**打戏技法知识库**（2026-10-15 学入的一批打戏技能索引）与**外部接口**（出口/端点/节点/派发口径全文）——技法与接口同册，查阅不必出本文件。

## 出口地址（唯一，钉死）
- **出口地址**：https://www.runninghub.cn/post/2110403291422220289
- **页面名称**：「H3官流（最强武戏）」（2026-10-19 助手开页核对、与页面标题一致，页面作者 onlyno999）
- **工作流 ID**：`2110403291422220289`（workflow 端点，本流 29 节点全在 115–179）
- **核对规矩**：以后凡走 H3XN 开始做片，派发前必须先核对地址／名称／ID 三项，任一对不上，停下报用户、不许建单。本地址不可改；各线出口严禁互切、混用（H3XG＝2110385615559806978 背后是另一个 API 模型）。

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
3. 拉玄幻仙侠战斗导演（组件三，独立仓、各自在线更新——与组件一、二同一规矩，互不相干）：`git clone https://github.com/lixiaoxiao9888-create/xuanhuan-combat-director.git ~/repos/xuanhuan-combat-director`（源克隆常驻此路径），把仓内 `xuanhuan-combat-director/` 目录放进宿主技能目录（本机：`~/workspace/skills/xuanhuan-combat-director/`，SKILL.md＋references 8 个规则库＋scripts 自检脚本）。**更新法**：在源克隆 `git pull` 后，把子目录整目录同步覆盖技能目录副本——组件三永远从它自己的上游仓更新，不从 H3XN 包内副本反向同步（包内 `references/skills/` 的技法快照不含组件三本体）。
4. 云端工作流激活（一次性）：工作流 `2110403291422220289` 若探针返回 **810**，须先在 RunningHub 网页打开并**运行一次**激活（之后回 803 即可派发）。激活是账号侧动作，Agent 只探针确认状态，不代跑。

## Tooling
- 西瓜本体：`~/workspace/xigua-drama-agent`（FastAPI :5678＋React 前端；本 Agent 只用其前半截流水线，不用它的本地 ComfyUI 算力）。
- 动作导演：技能 `fight-prompt-director`（本机 `~/workspace/skills/fight-prompt-director/`）。
- 玄幻仙侠导演：技能 `xuanhuan-combat-director`（本机 `~/workspace/skills/xuanhuan-combat-director/`；源仓 lixiaoxiao9888-create/xuanhuan-combat-director，源克隆常驻 `~/repos/xuanhuan-combat-director/`，各自 git pull 更新，装入时基线 V2.6.0／7a05678）。
- 打戏工艺规程（包内整合，本包的方法层）：`references/fight_craft.md`（技能 `fight-craft-onlyno999` 的包内整合版，与包外同名技能同源——八包蒸馏的写词七步＋落词八项自检；本包写动作段必过此规程当质检门，深查再回各源包）。
- 台词细化（包内整合）：`references/skills/minimaxh3-dialogue-refine/`（MINIMAXH3 格式动作/语气/台词细化 v1.0.0，2026-10-15 用户令同步入包）——本包的戏若带对白（喊招、战前对话、打斗中喊话），台词一律先过它：台词当时间线动作写进分镜、说话人 (Sx) 全片绑定一致、语气靠动作带、每镜补约束防乱说话；无对白的纯打斗段不用它。
- 打戏技法知识库（同作者/同批学入，按需查阅、不是组件、不改派发口径）：`seedance-combat-prompt`（二次元打戏：完播率公式、开局冲击、近景对招招式序列化、流派技法与兵器库）、`seedance-high-impact-combat-GFSM`（4–15s 高密度近身：空间三锚、攻防成对、物理闭环）、`ai-spell-impact-lens`（施法冲击帧＋震屏回归两式）、`seedance-fantasy-ultimate-prompt`（九大属性大招库）、`ai-cinematic-shot-craft`（国风漫剧镜头工艺：类型/质感/特效元件/节奏八卷）、`real-combat-director`（真人写实打斗：11 环动力链、防守三态、多人调度）、`short-drama-director`（漫剧老李全流程 V6.9.9：门控剧本、资产锁、机检；其 H3 支线只作格式参考，派发仍走本包出口口径）。
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
   - 玄幻仙侠题材（修真/仙法/神魔/法术对轰）：动作段改由组件三 `xuanhuan-combat-director` 主导结构——三轮攻守骨架＋整秒细切＋收束协议先定，再回组件二补因果链细节；技法细节按需查包内知识库（`references/skills/`，大招查 fantasy-ultimate、施法爆发帧查 spell-impact-lens、近景序列化查 combat-prompt/GFSM）。Seedance 向的时间戳/格式习惯只借结构，落词仍按本包 H3 六段式与出口口径。
   - **工艺门（整合定版）**：动作段落词前后必过 `references/fight_craft.md` 的写词七步与落词八项自检（定档/骨架/序列化/空间与收束/特效与冲击帧/终结三段式/自检），缺项回炉再派；自检结论随派发档案留痕。
   - 打斗节奏铁律（用户定版）：速度写进提示词成为角色动作本身的迅猛节奏，全程高速一气呵成，绝无慢动作/定格/停顿；不许后期变速凑时长。
   - 角色长相只许引用参考图，不许用文字复述五官；签名造型逐项写死。
4. **派发前探针**：`bin/probe_step1.py` 确认 803；810 就停下报用户去网页运行一次，不许换出口顶替。
5. **派发**：`bin/dispatch_wf.py`——提示词同填 138.value 与 136.prompt；Standard 实例；记任务号。
6. **取回**：轮询到 SUCCESS 立即下载原片（原生尺寸交付，不裁不缩）。
7. **质检门**（自己跑完）：抽帧查脸对卡/造型/场景 1:1/无烧字水印；动作段逐拍核因果链有没有拍出来（漏拍、软打、慢镜都是病）；有对白时 ASR 核台词内容与次数；音频只许原生对白＋现场拟音，检出配乐/旁白＝污染；规格核时长/分辨率/帧率。
8. **交付**：转码收尾（H.264 High@L4.0、yuv420p、bt709、AAC LC 48kHz、剥元数据、+faststart、尺寸保持云端原生）→ 聊天附件＋Drive「成片」夹链接。

## 打戏技法知识库（2026-10-15 学入，**已全部整合进本包**）
今晚学入的打戏技能已全套 vendoring 进本包 `references/skills/`（随包自带、装到别处即齐全；各包同时保留包外独立安装，源头更新时先更新包外本体、再整目录同步覆盖本包副本）：`seedance-combat-prompt`、`seedance-fantasy-ultimate-prompt`、`ai-spell-impact-lens`、`seedance-high-impact-combat-GFSM`、`ai-cinematic-shot-craft`、`real-combat-director`、`short-drama-director`、`minimaxh3-dialogue-refine`（台词细化，2026-10-15 晚补入），外加蒸馏规程 `references/fight_craft.md`（包外技能名 fight-craft-onlyno999）。写词时按病症取用，只借技法与结构，不借别家的出口与格式口径：
- **开局慢热/前 2 秒没接触** → `seedance-combat-prompt` 开局冲击律（1.5s 内攻防接触）＋完播率公式自查。
- **打斗软、像推拿/相持发呆** → 组件三 `xuanhuan-combat-director` 整秒细切＋瞬发瞬收动词；写实题材查 `real-combat-director` 动力链。
- **近景对招写成「快速连击」这类空话** → `seedance-combat-prompt` 招式序列化（逐招点名＋落点＋防守反馈）或 GFSM 攻防成对。
- **人物打着打着跑散/瞬移** → GFSM 空间三锚点＋组件三收束协议（A 遗物定场/B 抛飞隔离/C 光粒湮灭/D 永动硬切）。
- **法术爆发没冲击力** → `ai-spell-impact-lens` 冲击帧＋震屏回归（单帧光爆，动作不停，不许演成慢镜/定格）。
- **终结技单薄** → `seedance-fantasy-ultimate-prompt` 属性大招库＋组件三反杀三段式（前摇蓄压→立体巨刃→横推碾压）。
- **画面廉价/塑料感** → `ai-cinematic-shot-craft` B 质感层＋G 特效元件层（一镜 1–2 个特效、三色控制）。

## 外部接口（本包唯一出口，与本文件同册）
- **出口**：RunningHub workflow `2110403291422220289`（武打设计专用），端点 `POST /openapi/v2/run/workflow/2110403291422220289`；ai-app 通道 901 不用。
- **实例**：Standard（`instanceType=default`），用户当次点名才例外。
- **激活探针**：派发前 `bin/probe_step1.py` 零扣费查状态——803 已激活可派；810 须用户先在网页运行一次，Agent 不代跑、不换出口。
- **节点图谱**：全流 29 节点全在 115–179；派发口以本文件「云端派发口」表为准（138.value＋136.prompt 双填定版；132 时长；115 画幅；129 种子；图槽 137/139/167/173；音频仅 148.audio 一个入口）；完整图谱与验证记录在 `references/node_map.md`。
- **原生规格**（回片实测）：768×1376 / 24fps / AAC 32kHz；交付保持原生尺寸、音频升 48kHz，其余按 Workflow 第 8 步转码收尾。
- **派发器**：`bin/dispatch_wf.py`（上传→建任务→轮询→SUCCESS 立即下载，results URL 约 24h 有效）；任务号逐单记入该片项目目录档案。
- **鉴权**：surrogate 凭据 `custom.runninghub`，脚本内封装，Key 不落盘、不进包、不进记忆。

## 铁律
1. 出片只许走 `2110403291422220289`；不许切去 H3XG 的 2110385615559806978 或任何其他出口——每个出口背后的 API 模型不一样。
2. 三个上游组件保持独立：西瓜本体、fight-prompt-director、xuanhuan-combat-director 各自是独立克隆、各自在线更新，本包不改它们、不把它们并进本包仓库。技法知识库各包是例外（用户 2026-10-15 令全部整合）：全套快照存 `references/skills/` 随包走，但只作技法参考、不升格为组件、不改其内容，更新走「包外本体→整目录同步」单向覆盖。
3. 每派必先免费探针；探针不过（810）就停，不许先派再说。
4. 动作段提示词必须过 fight-prompt-director 编排，不许手写简化版应付。
5. 三视图现成图只直用、不动图；缺什么图补画什么图。
6. 提示词双入口（138/136）**双填已定版**（2026-10-15 首派回片验证：同文两处同填、照词执行无误，细节见 `references/node_map.md`）；后续派发照此常设，不再逐次议。
7. 质检由 Agent 全跑完、结论先行汇报；**回片有问题先报用户、由用户决定要不要重拍/重派，Agent 不许擅自拍第 2 版**（用户 2026-10-15 明令，覆盖一切「质检不过自己重跑」的旧口径）。
