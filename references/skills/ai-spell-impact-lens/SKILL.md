---
name: ai-spell-impact-lens
description: 将"冲击帧"与"震屏回归"两种AI漫剧爆发镜头技法整理为可复用提示词模板，对接分镜9字段，用于施法、爆炸、能量释放类镜头的Seedance提示词生成。
category: 分镜运镜灯光
version: 1.0.0
author: 学习整理自 AIGC魔法师系 视频教程
---

# AI漫剧施法爆发镜头

> 适用：AI 漫剧 / 3D 国漫 / 仙侠/玄幻施法、法术爆发、能量释放、爆炸类镜头
> 全局规则：无 BGM、无字幕

## 核心原理

AI 漫剧施法像放烟花，爆发瞬间靠两个镜头技法提升冲击力：
1. **冲击帧**：画面在能量释放瞬间"炸开"。
2. **震屏**：摄像机随爆炸剧烈抖动并缓慢回归平稳。


## 技法一：冲击帧

### 定义
爆炸/施法瞬间的定格帧：画面全屏闪白，能量从中心点高速炸开，冲击波呈圆环状向外扩散，同时地面尘土、碎石、残渣被气浪一起掀起。

### 分镜字段对应

| 字段 | 关键词写法 |
|------|------------|
| 时码 | 0-0.5s 为冲击帧核心；可占整段 15s 镜头的前 1/3 |
| 景别 | 大全景/全景 → 突出冲击波扩散；特写 → 强调中心炸开 |
| 全局画质 | cinematic 3D anime, 4K UHD, motion blur, volumetric light |
| 人物材质 | （若有人物）衣袂被气浪向后撕扯，发丝飞扬，受击姿态 |
| 核心特效 | white flash, radial shockwave ring, debris explosion, dust kickup, ground cracks |
| 构图 | 中心构图 / 对称构图，能量点位于画面黄金分割中心 |
| 机位 | 低角度仰拍 / 平视微仰，让地面尘土向镜头扑来 |
| 动作 | 施法者手臂/法器前推 → 能量从掌心/法器中心爆发 |
| 音效 | 提示词中不写音效，后期单独设计；如需描述可用 "impact silent then ringing" |

### Seedance 提示词模板

```
Extreme close-up of a Daoist caster's palm thrusting forward, sudden full-screen white flash, energy erupts from center point at extreme speed, radial shockwave ring expanding outward, ground dust and gravel debris blasted upward, motion blur, volumetric light, cinematic 3D anime style, 4K UHD --ar 9:16 --no bgm subtitle
```


## 技法二：震屏回归平稳

### 定义
爆炸瞬间摄像机剧烈震动，震动幅度先大后小，持续约 0.3 秒，随后缓慢恢复稳定，最后回归平稳画面。

### 分镜字段对应

| 字段 | 关键词写法 |
|------|------------|
| 时码 | 0-0.3s 剧烈震屏；0.3-2.0s 缓慢回稳；2.0s 后完全平稳 |
| 景别 | 保持原景别不变（震屏不改变景别，只改变机位稳定性） |
| 全局画质 | handheld camera feel, jitter smoothing, post-stabilize gradual |
| 核心特效 | camera shake, motion blur, lens blur during shake |
| 构图 | 震屏时中心点偏移后回中；回稳后恢复原始构图 |
| 机位 | 手持机位/肩扛机位 → 震屏自然；回稳后恢复固定机位 |
| 动作 | 画面内容保持静止或慢动作，让震屏本身成为动态 |
| 后续 | 回归平稳后可接角色反应/烟尘散去 |

### Seedance 提示词模板

```
Over-the-shoulder shot, moment of spell detonation, camera violently shakes with large-to-small amplitude for 0.3 seconds, then slowly stabilizes back to a smooth steady frame, dust settling, cinematic 3D anime style, 4K UHD --ar 9:16 --no bgm subtitle
```


## 组合连招：冲击帧 + 震屏 + 回归平稳

标准三拍子（用于 4-15s 镜头）：
1. **0.0-0.5s**：冲击帧 —— 闪白、中心炸开、圆环冲击波、尘土掀起
2. **0.5-0.8s**：震屏 —— 摄像机剧烈抖动，幅度先大后小
3. **0.8-2.0s**：回归平稳 —— 烟尘缓缓落下，画面恢复稳定，接角色反应

### 完整 Seedance 提示词示例

```
Extreme close-up of a glowing spell seal erupting, full-screen white flash, energy core blasts outward at high speed, concentric shockwave rings expand across the frame, dust and rock debris lifted from the ground, camera violently shakes large-to-small for 0.3s then slowly stabilizes, lingering smoke particles drifting in soft light, cinematic 3D anime style, 4K UHD, volumetric light, motion blur --ar 9:16 --no bgm subtitle
```


## 与现有技能的协作

| 现有技能 | 分工 |
|----------|------|
| ai-storyboard-camera-lighting | 选景别、运镜、灯光（侧逆光/丁达尔） |
| deepwhite-shotlist-builder-zh-user | 把本技能的冲击帧+震屏写成完整分镜表 |
| seedance-high-impact-combat-GFSM | 近身打斗终结战可叠加本技能的震屏 |
| ai-film-methodology | 长片/漫剧整体流程中安排爆发节奏 |


## 注意事项

- 冲击帧和震屏都是"瞬时技法"，不要整段 15s 都在闪白抖动，否则观众疲劳。
- 震屏幅度"先大后小"是关键词，提示词里要写出来。
- "回归平稳"不是突然卡住，而是"缓慢恢复稳定"，保留一点余震感。
- 无 BGM、无字幕：Seedance 提示词用 `--no bgm subtitle` 或在描述中避免。


## 触发方式

用户输入以下任意意图时调用本技能：
- "施法爆发镜头怎么写"
- "冲击帧提示词"
- "震屏镜头"
- "法术爆炸分镜"
- "做分镜时加一个施法爆发"
