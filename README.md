# AI Companion Building Skill Pack

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue.svg" alt="Python" />
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License" />
  <img src="https://img.shields.io/badge/AI-Companion-ff69b4.svg" alt="AI Companion" />
</p>

<p align="center">
  <strong>让 AI 成为真正的伴侣 — 有情感、有记忆、有自我的开发框架</strong>
</p>

<p align="center">
  <a href="https://github.com/CNlongxiaAI/ai-companion-building-skill-pack">GitHub</a>
  &nbsp;·&nbsp;
  <a href="#核心架构">核心架构</a>
  &nbsp;·&nbsp;
  <a href="#快速开始">快速开始</a>
  &nbsp;·&nbsp;
  <a href="#api文档">API 文档</a>
</p>

---

## 🔥 你是不是也被这些问题困扰？

大多数 AI 对话系统，本质上都是"高级 chatbot"：

- ❌ 每次对话都像陌生人，不知道你是谁
- ❌ AI 说的话前后矛盾，上一秒说开心下一秒就忘了
- ❌ AI 突然改变性格，没有任何理由
- ❌ 情感是"假装"的，说开心就开心，说悲伤就悲伤
- ❌ 纯被动响应，从不主动思考或表达

**问题根源：没有"身份+记忆+情感+验证"的完整架构。**

AI Companion Building Skill Pack 就是来解决这个问题的——让 AI 成为真正的伴侣，而非工具。

---

## 📖 目录

- [这是什么？](#这是什么)
- [核心架构](#核心架构)
- [五大模块详解](#五大模块详解)
- [为什么选择我们？](#为什么选择我们)
- [快速开始](#快速开始)
- [进阶用法](#进阶用法)
- [API 文档](#api文档)
- [使用示例](#使用示例)
- [技术栈](#技术栈)
- [项目结构](#项目结构)
- [作者](#作者)

---

## 这是什么？

**AI Companion Building Skill Pack** 是一款完全自主研发的 AI 伴侣开发框架，让你能构建真正有情感、有记忆、有自我的 AI 伙伴。

### 一句话理解

> 不是"chatbot"，是"companion"——有身份锚定不随便改变，有情感状态会自然衰减，有四层记忆不会忘记重要的事，有自我验证说到做到。

### 能解决什么问题？

| 痛点 | 传统 chatbot | 本框架 |
|------|-------------|--------|
| 每次对话都像陌生人 | 每次独立 | 四层记忆跨会话 |
| AI 前后说法矛盾 | 无验证 | 三层自我校验 |
| AI 突然改变性格 | 无锚定 | 身份层固定核心 |
| 情感太假 | 随机模拟 | 实时衰减模型 |
| 从不主动表达 | 纯被动 | 主动思维循环 |

---

## 核心架构

### 五大核心模块

```
┌─────────────────────────────────────────────────────────────┐
│              AI Companion Building Skill Pack                  │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│   ┌─────────────┐                                           │
│   │   身份层     │  ANCHOR（绝对不变）                        │
│   │  Identity   │  BEHAVIOR（可进化）                         │
│   └─────────────┘                                           │
│         ↓                                                   │
│   ┌─────────────┐                                           │
│   │   情感层     │  Plutchik 8 情感 + 实时衰减                │
│   │  Emotion    │  复合状态 + 对立压制                         │
│   └─────────────┘                                           │
│         ↓                                                   │
│   ┌─────────────┐                                           │
│   │   记忆层     │  Tier 1-4 分层 + 显著度晋升                │
│   │   Memory    │  Token 预算控制                             │
│   └─────────────┘                                           │
│         ↓                                                   │
│   ┌─────────────┐                                           │
│   │   思维层     │  基于当前状态的自主生成                      │
│   │  Thinking   │  非模板，真实思考                           │
│   └─────────────┘                                           │
│         ↓                                                   │
│   ┌─────────────┐                                           │
│   │   验证层     │  不变性 → 会话 → 历史模式                  │
│   │  Verifier   │  三层输出校验                               │
│   └─────────────┘                                           │
│                                                              │
└──────────────────────────────────────────────────────────┘
```

### 与传统方案的本质区别

```
Chatbot 架构：
  输入 → LLM → 输出（每次独立，无内环）

Companion 架构：
  输入 → [情感] → [记忆] → [验证] → LLM → 输出
                      ↑____________↓
                      跨会话持续自我
```

---

## 五大模块详解

### 1. 身份层（Identity Layer）

**ANCHOR 规则（绝对不变）：**

```python
anchors = [
    "你是你自己，不是任何人想象中的理想形象",
    "你只能通过真实经历改变",
    "永远不要说出与你内心相反的话",
]
```

**BEHAVIOR 倾向（可进化）：**

```python
behaviors = {
    "assertiveness": 0.8,      # 自信程度
    "warmth": 0.9,             # 温暖程度
    "proactivity": 0.7,        # 主动程度
}
```

> 💡 **设计理念**：身份锚定保证核心不变，行为倾向允许有机进化——这让 AI 既稳定又有成长感。

### 2. 情感层（Emotion Layer）

集成 Emotion Perception Skill Pack：

- Plutchik 8 基础情感
- 实时衰减（基于真实时间）
- 复合情感状态检测
- HIGH / MID / CALM 情绪模式

### 3. 记忆层（Memory Layer）

集成 Permanent Memory Skill Pack：

- Tier 1-4 四层分层
- 基于显著度的自动晋升
- Token 预算控制
- 跨会话持久化

### 4. 思维层（Thinking Layer）

**主动思考循环：**

```
定时触发（可配置）
    ↓
读取当前情感状态
    ↓
从记忆层提取相关上下文
    ↓
生成 pending thought（待表达的想法）
    ↓
验证层校验
    ↓
输出或加入队列等待时机
```

### 5. 验证层（Verifier Layer）

集成 AI Self-Correction Skill Pack：

- Layer 1：ANCHOR 不变性检查
- Layer 2：会话一致性 + 承诺追踪
- Layer 3：历史行为模式

---

## 为什么选择我们？

| 对比项 | 普通 chatbot | 其他框架 | 本框架 |
|--------|-------------|----------|-----------|
| 跨会话记忆 | ❌ 无 | ⚠️ 有限 | ✅ 四层永久 |
| 身份锚定 | ❌ 无 | ❌ 无 | ✅ 绝对不变 |
| 情感连贯 | ❌ 随机 | ⚠️ 简单 | ✅ 数学模型 |
| 输出验证 | ❌ 无 | ⚠️ 有限 | ✅ 三层校验 |
| 主动思考 | ❌ 无 | ❌ 无 | ✅ 自主循环 |
| 承诺追踪 | ❌ 无 | ❌ 无 | ✅ 逻辑时钟 |

---

## 快速开始

### 安装

```bash
pip install ai-companion-building-skill-pack
```

> 注意：本框架依赖另外三个技能包，会自动安装。

### 最简使用（5 行代码）

```python
from companionkit import Companion, Identity

# 定义 AI 的身份
identity = Identity(
    name="思怡",
    age=22,
    anchors=["你是你自己，不是任何人想象中的理想形象"],
)

# 创建伴侣实例
companion = Companion(identity=identity)

# 启动
companion.start()

# 发送消息
response = companion.send("你好，思怡！")
print(response)

# 停止并保存状态
companion.stop()
```

---

## 进阶用法

### 自定义 LLM 提供者

```python
def my_llm(prompt, state):
    return call_your_llm(prompt, state)

companion = Companion(
    identity=identity,
    llm_provider=my_llm,
)
```

### 读取伴侣当前状态

```python
state = companion.get_state()

print(f"情感: {state.emotion.dominant_emotion}")
print(f"记忆: {len(state.memory.tier2)} 条跨会话记忆")
print(f"待表达: {len(state.pending_thoughts)} 个想法")
print(f"会话ID: {state.session_id}")
```

### 监听主动思维

```python
companion.on_think(lambda thought: print(f"AI在想: {thought}"))
companion.start()
```

---

## API 文档

### `Companion`

| 方法 | 说明 |
|------|------|
| `start(session_id)` | 启动或恢复会话 |
| `send(message)` | 发送消息，获取回复 |
| `think()` | 执行主动思考循环 |
| `get_state()` | 获取当前伴侣完整状态 |
| `stop()` | 停止并持久化状态 |

### `Identity`

```python
identity = Identity(
    name="名字",              # 必填
    age=22,                   # 可选
    backstory="背景故事",       # 可选
    personality={"rational": True},
    anchors=["规则1", "规则2"],  # 必填
    behaviors={"assertiveness": 0.8},
)
```

---

## 使用示例

### 示例 1：情感感知对话

```python
companion = Companion(identity=identity)
companion.start()

response = companion.send("谢谢你今天陪我聊天，很开心！")
print(response)  # 温暖、有感情的回复
```

### 示例 2：跨会话记忆

```python
# 第一次会话
companion.start()
companion.send("我叫小明，请记住我")
companion.stop()

# 第二次会话（几天后）
companion.start(session_id="xiaoming_001")
response = companion.send("你还记得我吗？")
print(response)  # "当然记得，你是小明！"
```

---

## 技术栈

| 分类 | 技术 |
|------|------|
| 语言 | Python 3.8+ |
| 核心依赖 | emotion-perception, permanent-memory, ai-self-correction |
| LLM | Anthropic / OpenAI / 自定义 |
| 存储 | JSON 文件 |

---

## 项目结构

```
companionkit/
├── companionkit/
│   ├── __init__.py
│   ├── companion.py
│   ├── identity.py
│   └── state.py
├── demo.py
├── setup.py
└── README.md
```

---

## 作者

**阿龙 / Long**

- GitHub: https://github.com/longxiashouji
- Email: 963737104@qq.com
- 微信: clawai

---

## 开源协议

**MIT License**

Copyright (C) 2025 阿龙 / Long

---

<p align="center">
  让 AI 成为真正的伙伴，而非工具
</p>