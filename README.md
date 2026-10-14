# H3XN-onlyno999

武打短剧生产 Agent：**西瓜短剧 Agent 前半截（剧本/分镜/提示词流水线）＋ fight-prompt-director 动作导演（打斗提示词编排）＋ RunningHub 武打设计专用工作流 2110403291422220289 出片**的独立技能包。

- 第一次安装先分别拉取两个上游组件（见 SKILL.md「第一次安装」）：西瓜本体 `zjs134679-sketch/xigua-drama-agent`、动作导演技能 `irenerachel/fight-prompt-director`——两者都是独立仓库、各自在线更新，本包不包含它们的代码。
- 出片只走云端工作流 `2110403291422220289`（武打设计专用出口），节点图谱在 `references/`，派发/探针/普查脚本在 `bin/`，鉴权走 RunningHub 凭据（不含任何密钥）。
- 与 H3XG-onlyno999 是两条独立的线：出口不同（2110403291422220289 vs 2110385615559806978）、背后的 API 模型不同、节点图谱不同，严禁混用。

触发词：H3XN / /H3XN-onlyno999 / 用 H3XN 出片。
