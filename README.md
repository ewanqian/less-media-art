# 少媒体艺术 | Less-Media Art

[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/)
[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Live-brightgreen)](https://ewanqian.github.io/less-media-art)
[![Open Source](https://img.shields.io/badge/Open%20Source-%E2%9D%A4-blue.svg)](https://github.com/ewanqian/less-media-art)
[![Research Framework](https://img.shields.io/badge/Type-Research%20Framework-orange.svg)]()

> **一个关于限制、本地与反思的数字艺术开放研究框架**

---

## 核心陈述

### 少媒体，不是一种风格，而是一种质问。

在生成式AI以生产力和奇观席卷一切的当下，我们选择追问：**当创作变得无限便捷时，我们失去了什么？**

这是一个开源的研究框架，邀请你进行一场反向实践：通过主动地、有意识地施加限制，来重新触摸创作的核心。

---

## 什么是"少媒体艺术"？

**少媒体艺术**并非一个宣言式的"学派"，也非一种固定的视觉风格。它是一个**开放的、持续自我质疑的研究框架**，源于对当下数字艺术生产范式的深度关切。

其核心在于：在生成式人工智能以"无限可能性"和"即时生产力"塑造主流艺术话语的今天，我们提出一种以**媒介减法**、**技术内省**与**过程显形**为核心的批判性实践。

### 核心对立面

- ❌ 无限生成 → ✅ **主动限制**
- ❌ 无缝融合 → ✅ **显形摩擦**
- ❌ 即时满足 → ✅ **过程可见**
- ❌ 云端依赖 → ✅ **本地运算**

---

## 核心理论概念

| 概念 | 简述 | 标签 |
|------|------|------|
| [媒介减法](https://ewanqian.github.io/less-media-art/theory/media-subtraction.html) | 主动减少可用媒介种类或功能的行为 | `核心` `方法论` |
| [约束美学](https://ewanqian.github.io/less-media-art/theory/aesthetics-of-constraint.html) | 人为限制如何成为创造力的催化剂 | `核心` `美学` |
| [本地性](https://ewanqian.github.io/less-media-art/theory/locality.html) | 坚持在个人设备上运算与存储的立场 | `核心` `伦理` |
| [过程显形](https://ewanqian.github.io/less-media-art/theory/process-visibilization.html) | 将隐藏的创作过程作为作品核心 | `核心` `方法论` |
| [技术内省](https://ewanqian.github.io/less-media-art/theory/technological-introspection.html) | 对创作工具本身的批判性审视 | `核心` `理论` |
| [后提示词工程](https://ewanqian.github.io/less-media-art/theory/post-prompt-engineering.html) | 将提示词本身作为反思对象 | `核心` `AI` |
| [摩擦](https://ewanqian.github.io/less-media-art/theory/friction.html) | "不顺畅"在数字创作中的价值 | `核心` `交互` |
| [小模型](https://ewanqian.github.io/less-media-art/theory/small-models.html) | 轻量级本地AI模型的美学意涵 | `技术` `本地` |
| [AI时代的创造力悖论](https://ewanqian.github.io/less-media-art/theory/ai-creativity-paradox.html) | 回应Lev Manovich关于AI与创造力的讨论 | `理论语境` `学术对话` |
| [对话式创作](https://ewanqian.github.io/less-media-art/theory/dialogic-creation.html) | AI作为提问者而非工具，通过对话显形思维 | `核心` `方法论` |

---

## 项目结构

```
less-media-art/
├── 📄 README.md                 # 本文件
├── 📁 docs/                     # 知识库（Markdown源文件）
│   ├── index.md                 # 首页内容
│   ├── 📁 theory/               # 理论词条
│   │   ├── media-subtraction.md
│   │   ├── aesthetics-of-constraint.md
│   │   ├── ai-creativity-paradox.md
│   │   └── ...
│   ├── 📁 methods/              # 方法工具箱
│   ├── 📁 archive/              # 案例档案
│   └── 📁 discussion/           # 讨论与议题
├── 📁 tools/                    # 研究工具
├── 📁 site/                     # 网站生成配置
└── 📁 Public/                   # 生成的网站（GitHub Pages）
```

---

## 快速开始

### 1. 阅读理论

从核心理论词条开始理解框架：

- [媒介减法](docs/theory/media-subtraction.md) — 理解"少"的哲学
- [AI时代的创造力悖论](docs/theory/ai-creativity-paradox.md) — 理解理论背景
- [约束美学](docs/theory/aesthetics-of-constraint.md) — 限制如何激发创造力

### 2. 搭建环境

```bash
# 安装 Ollama
brew install ollama

# 拉取轻量级模型
ollama pull llama3.2:3b

# 运行
ollama run llama3.2:3b
```

### 3. 尝试苏格拉底模式（推荐）

```bash
cd tools/constraint-cli
pip install -e .

# 启动十轮批判对话
constraint-cli --mode socratic --topic "你想探索的主题"
```

AI将扮演提问者，通过十轮深入对话帮助你反思，而不是直接给你答案。

### 4. 传统约束模式

```bash
constraint-cli --constraint "仅使用100个token" --log my-first-session.log
```

---

## 理论基底

### 🎨 观念艺术的遗产

继承并转换了索尔·勒维特"观念先于形式"的命题。在少媒体的语境下，"观念"体现在对**创作条件本身的先决性设置**上。

### 🔧 对"技术黑箱"的批判

借鉴弗里德里希·基特勒的媒介物质性思想，强调将技术过程从"黑箱"中拉回前台。

### 📐 "限制作为生成器"的美学传统

从乌力波到简约主义，主动设置的规则与限制长久以来被视为激发创造力的引擎。

### 🌐 后网络时代的"物性"回归

通过强调**本地计算的物质性**、**过程文件的唯一性**，以及**交互的笨拙与阻力**，重新为数字艺术注入可感知的"物性"。

### 🤖 AI时代的创造力反思

回应Lev Manovich等学者的研究（特别是《AI美学与人类中心主义的创造力神话》）：当AI可以生成"比蒙德里安更像蒙德里安"的作品时，艺术家的价值何在？

我们的答案是：**显形创作过程，重新定义人类作者性**。

不是对抗AI，而是与AI对话；不是追求效率，而是追求思考；不是让AI替你创作，而是让AI帮你看见自己的思维。

---

## 如何参与

| 方式 | 描述 | 适合人群 |
|------|------|----------|
| 📖 **阅读与思考** | 从[理论词条](docs/theory/)开始 | 所有人 |
| 🛠️ **实践与记录** | 使用[方法工具箱](docs/methods/)进行创作 | 创作者 |
| 📤 **提交案例** | 将实践提交到[案例档案](docs/archive/) | 实践者 |
| 💬 **批判与讨论** | 在[讨论区](docs/discussion/)发起议题 | 研究者 |

---

## 网站构建

```bash
cd site
pip install markdown
python build.py
```

GitHub Actions 会自动部署到 GitHub Pages。

---

## 许可证

- **内容**: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)
- **代码**: [MIT License](LICENSE)

---

<p align="center">
  <i>这是一个未完成的、始终处于构建中的思想模型。</i><br>
  <i>欢迎您成为这个研究网络的构建者之一。</i>
</p>

<p align="center">
  <a href="https://ewanqian.github.io/less-media-art">🌐 访问网站</a> •
  <a href="https://github.com/ewanqian/less-media-art">💻 GitHub</a> •
  <a href="docs/theory/">📚 理论</a> •
  <a href="docs/methods/">🛠️ 方法</a>
</p>
