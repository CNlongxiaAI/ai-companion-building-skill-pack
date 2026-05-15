# AI Companion Building Skill Pack

<p align="center">
  <strong>让 AI 成为真正的伴侣 — 有情感、有记忆、有自我的开发框架</strong>
</p>

<p align="center">
  <a href="https://github.com/CNlongxiaAI/ai-companion-building-skill-pack">GitHub</a>
</p>

---

## 这是什么？

**AI Companion Building Skill Pack** 是一款完全自主研发的 AI 伴侣开发框架，让你能构建真正有情感、有记忆、有自我的 AI 伙伴。

### 能解决什么问题？

| 问题 | 本框架如何解决 |
|------|---------------------|
| AI 太理性像机器人？ | 情感引擎让 AI 有温度 |
| AI 每次对话都像陌生人？ | 四层记忆跨会话记住你 |
| AI 前后说法自相矛盾？ | 自我验证三层校验 |

### 一句话理解

不是"chatbot"，是"companion"——有身份锚定不随便改变，有情感状态会自然衰减，有四层记忆不会忘记重要的事。

---

## 快速开始

### 安装

```bash
pip install ai-companion-building-skill-pack
```

### 基础使用

```python
from companionkit import Companion, Identity

identity = Identity(name="思怡", anchors=["你是你自己"])
companion = Companion(identity=identity)
companion.start()
print(companion.send("你好！"))
```

---

## 作者

**阿龙 / Long**
- GitHub: https://github.com/longxiashouji
- Email: 963737104@qq.com
- 微信: clawai

## 开源协议

**MIT License**
Copyright (C) 2025 阿龙 / Long
