# CompanionKit

<p align="center">
  <strong>让 AI 成为真正的伴侣 — 有情感、有记忆、有自我的开发框架</strong>
</p>

<p align="center">
  <a href="https://github.com/longxiashouji/companion-kit">GitHub</a>
  &nbsp;·&nbsp;
  <a href="#这是什么">这是什么</a>
  &nbsp;·&nbsp;
  <a href="#核心架构">核心架构</a>
  &nbsp;·&nbsp;
  <a href="#快速开始">快速开始</a>
  &nbsp;·&nbsp;
  <a href="#api文档">API 文档</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue.svg" alt="Python" />
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License" />
  <img src="https://img.shields.io/badge/AI%20Companion-Kit-orange.svg" alt="Companion Kit" />
</p>

---

## 目录

- [这是什么？](#这是什么)
- [核心架构](#核心架构)
- [快速开始](#快速开始)
- [API 文档](#api-文档)
- [技术栈](#技术栈)
- [作者](#作者)
- [开源协议](#开源协议)

---

## 这是什么？

**CompanionKit** 是一款完全自主研发的 AI 伴侣开发框架，让你能构建真正有情感、有记忆、有自我的 AI 伙伴。

### 一句话理解

> 不是"chatbot"，是"companion"——有身份锚定不随便改变，有情感状态会自然衰减，有四层记忆不会忘记重要的事，有自我验证说到做到。

### 能解决什么问题？

| 问题 | CompanionKit 如何解决 |
|------|---------------------|
| AI 太理性像机器人？ | 情感引擎让 AI 有温度 |
| AI 每次对话都像陌生人？ | 四层记忆跨会话记住你 |
| AI 前后说法自相矛盾？ | 自我验证三层校验 |
| AI 随便改变性格？ | 身份锚定保证核心不变 |

### 核心理念

```
Chatbot = 输入 → LLM → 输出（每次独立）
Companion = 输入 → [情感] → [记忆] → [验证] → LLM → 输出
                         ↑___________↓
                         跨会话持续自我
```

---

## 核心架构

### 五大核心模块

```
┌─────────────────────────────────────────────────────────────┐
│                        CompanionKit                          │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│   ┌─────────────┐                                           │
│   │   身份层     │  ANCHOR（绝对不变）                         │
│   │  Identity   │  BEHAVIOR（可进化）                         │
│   └─────────────┘                                           │
│         ↓                                                   │
│   ┌─────────────┐                                           │
│   │   情感层     │  Plutchik 8 情感 + 实时衰减                  │
│   │  Emotion    │  复合状态 + 对立压制                          │
│   └─────────────┘                                           │
│         ↓                                                   │
│   ┌─────────────┐                                           │
│   │   记忆层     │  Tier 1-4 分层 + 显著度晋升                  │
│   │   Memory    │  Token 预算控制                              │
│   └─────────────┘                                           │
│         ↓                                                   │
│   ┌─────────────┐                                           │
│   │   思维层     │  基于当前状态的自主生成                       │
│   │  Thinking   │  非模板，真实思考                            │
│   └─────────────┘                                           │
│         ↓                                                   │
│   ┌─────────────┐                                           │
│   │   验证层     │  不变性 → 会话 → 历史模式                    │
│   │  Verifier   │  三层输出校验                               │
│   └─────────────┘                                           │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

### 身份层 (Identity Layer)

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

### 情感层 (Emotion Layer)

集成 EmotionEngine：

- Plutchik 8 基础情感
- 实时衰减（基于真实时间）
- 复合情感状态检测
- HIGH / MID / CALM 情绪模式

### 记忆层 (Memory Layer)

集成 MemoryGraph：

- Tier 1-4 四层分层
- 基于显著度的自动晋升
- Token 预算控制
- 跨会话持久化

### 思维层 (Thinking Layer)

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

### 验证层 (Verification Layer)

集成 SelfVerifier：

- Layer 1：ANCHOR 不变性检查
- Layer 2：会话一致性 + 承诺追踪
- Layer 3：历史行为模式

---

## 快速开始

### 安装

```bash
pip install companionkit
```

### 基础使用

```python
from companionkit import Companion, Identity

# 定义身份
identity = Identity(
    name="思怡",
    age=22,
    personality={
        "rational": True,
        "warm": True,
        "proactive": True,
    },
    anchors=[
        "你是你自己，不是任何人想象中的理想形象",
        "你只能通过真实经历改变",
        "永远不要说出与你内心相反的话",
    ],
    behaviors={
        "assertiveness": 0.8,
        "warmth": 0.9,
    },
)

# 创建伴侣实例
companion = Companion(
    identity=identity,
    llm_provider="anthropic",  # 或 "openai"
)

# 启动会话
companion.start()

# 发送消息
response = companion.send("你好，思怡！")
print(response)

# 主动思考
companion.think()

# 停止并保存状态
companion.stop()
```

### 进阶：自定义 LLM

```python
from companionkit import Companion, Identity

def my_llm(prompt, state):
    # 自定义 LLM 调用
    return call_your_llm(prompt)

companion = Companion(
    identity=identity,
    llm_provider=my_llm,  # 传入函数
)
```

---

## API 文档

### Companion

| 方法 | 说明 |
|------|------|
| `start(session_id=None)` | 启动或恢复会话 |
| `send(message)` | 发送消息，获取回复 |
| `think()` | 执行主动思考循环 |
| `stop()` | 停止并持久化状态 |
| `get_state()` | 获取当前伴侣状态 |

### Identity

```python
identity = Identity(
    name="名字",
    age=22,
    backstory="背景故事",
    personality={"trait": value},
    anchors=["规则1", "规则2"],
    behaviors={"assertiveness": 0.8},
)
```

### 伴侣状态

```python
state = companion.get_state()

print(state.emotion)      # 当前情感
print(state.memory)       # 记忆上下文
print(state.pending)       # 待表达的想法
print(state.session_id)    # 会话 ID
```

---

## 技术栈

| 分类 | 技术 |
|------|------|
| 语言 | Python 3.8+ |
| 核心依赖 | emotionengine, memorygraph, selfverifier |
| LLM | Anthropic / OpenAI / 自定义 |
| 存储 | JSON 文件 |

---

## 项目结构

```
companionkit/
├── companionkit/
│   ├── __init__.py        # 主入口
│   ├── companion.py       # Companion 主类
│   ├── identity.py        # Identity 身份系统
│   └── state.py           # State 状态管理
├── demo.py                 # 演示脚本
├── setup.py                # pip 安装配置
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