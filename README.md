# less-media-art
一个关于限制、本地与反思的数字艺术研究框架


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
│   │   └── ...
│   ├── 📁 methods/              # 方法工具箱
│   │   ├── environment-setup.md
│   │   ├── constraint-patterns.md
│   │   └── documentation-guide.md
│   ├── 📁 archive/              # 案例档案
│   └── 📁 discussion/           # 讨论与议题
├── 📁 tools/                    # 研究工具
│   └── 📁 constraint-cli/       # 约束命令行工具
├── 📁 site/                     # 网站生成配置
│   ├── build.py                 # 静态站点生成器
│   └── README.md
├── 📁 Public/                   # 生成的网站（GitHub Pages）
└── 📁 .github/
    └── 📁 workflows/
        └── deploy.yml           # 自动部署配置
```

---

## 快速开始

### 1. 阅读理论

从核心理论词条开始理解框架：

- [媒介减法](docs/theory/media-subtraction.md) — 理解"少"的哲学
- [约束美学](docs/theory/aesthetics-of-constraint.md) — 限制如何激发创造力
- [本地性](docs/theory/locality.md) — 为什么选择本地运算

### 2. 搭建环境

按照[环境搭建指南](docs/methods/environment-setup.md)配置本地AI创作环境：

```bash
# 安装 Ollama
brew install ollama

# 拉取轻量级模型
ollama pull llama3.2:3b

# 运行
ollama run llama3.2:3b
```

### 3. 开始实践

使用我们的研究工具进行第一次约束创作：

```bash
cd tools/constraint-cli
pip install -e .
constraint-cli --constraint "仅使用100个token" --log my-first-session.log
```

### 4. 提交案例

按照[案例提交规范](docs/methods/documentation-guide.md)记录并分享你的实践。

---

## 理论基底

少媒体艺术的实践与思考，建基于以下几条相互交织的线索：

### 🎨 观念艺术的遗产

我们继承并转换了索尔·勒维特"观念先于形式"的命题。在少媒体的语境下，"观念"体现在对**创作条件本身的先决性设置**上——为何选择此种媒介？为何施加此项限制？对这些问题的审慎回答，构成了作品不可见但至关重要的观念内核。

### 🔧 对"技术黑箱"的批判

借鉴了弗里德里希·基特勒的媒介物质性思想和当下对算法文化的批判，少媒体艺术强调将技术过程从"黑箱"中拉回前台。**使用本地、轻量、可审计的模型**，正是为了恢复对创作工具的物质性与政治性的认知，对抗云服务与大型模型带来的同质化效率与认知遮蔽。

### 📐 "限制作为生成器"的美学传统

从文学领域的"乌力波"（Oulipo）到音乐领域的简约主义，主动设置的规则与限制长久以来被视为激发创造力的引擎。少媒体艺术将这一传统置于数字AI创作的语境中，探究在"智能"工具面前，**人为约束如何成为保持作者主体性与批判意识的必要手段**。

### 🌐 后网络时代的"物性"回归

在数字图像近乎无限复制与传播的当下，少媒体艺术通过强调**本地计算的物质性**（硬件、电量、时间消耗）、**过程文件的唯一性**（特定环境生成的日志），以及**交互的笨拙与阻力**，试图重新为数字艺术注入一种可感知的"物性"与"事件性"。

---

## 如何参与

我们邀请您以**共同研究者**的身份参与，而非信徒或学生。

### 参与路径

| 方式 | 描述 | 适合人群 |
|------|------|----------|
| 📖 **阅读与思考** | 从[理论词条](docs/theory/)开始，理解框架的核心概念 | 所有人 |
| 🛠️ **实践与记录** | 使用[方法工具箱](docs/methods/)进行创作，详细记录过程 | 创作者 |
| 📤 **提交案例** | 将您的实践按规范提交到[案例档案](docs/archive/) | 实践者 |
| 💬 **批判与讨论** | 在[讨论区](docs/discussion/)发起议题或回应他人 | 研究者 |
| 🔧 **工具构建** | 开发新的极简软件工具或脚本 | 开发者 |

### 内容贡献指南

- 所有内容使用 **Markdown** 格式
- 遵循[文档规范](docs/methods/documentation-guide.md)
- 通过 Pull Request 提交修改
- 保持学术严谨性与开放性

---

## 研究工具

### 🔨 constraint-cli

一个极简的命令行工具，用于在约束条件下与本地AI模型对话。

```bash
# 安装
cd tools/constraint-cli
pip install -e .

# 使用示例
constraint-cli --constraint "仅使用100个token" --log session.log
constraint-cli --constraint "禁止用形容词" --model llama3.2:3b
constraint-cli --interactive --constraints-file constraints.yaml
```

**核心特性：**
- ✅ 本地运行，无需联网
- ✅ 可配置的约束规则
- ✅ 完整的会话日志记录
- ✅ 支持多种本地模型（通过 Ollama）

详见 [tools/constraint-cli/README.md](tools/constraint-cli/)

---

## 网站构建

本项目使用自定义的极简静态站点生成器将 Markdown 转换为 HTML。

### 本地构建

```bash
cd site
pip install markdown
python build.py
```

生成的网站位于 `Public/` 目录。

### 本地预览

```bash
cd Public
python -m http.server 8000
```

访问 http://localhost:8000

### 自动部署

GitHub Actions 工作流会在每次 push 到 main 分支时自动构建并部署到 GitHub Pages。

---

## 学术引用

如果您在研究中引用了本项目，请使用以下格式：

```bibtex
@misc{lessmediaart2025,
  title={少媒体艺术：一个开放的研究框架},
  author={少媒体艺术研究社区},
  year={2025},
  url={https://ewanqian.github.io/less-media-art}
}
```

---

## 理论基础与参照系

### 艺术史/理论
- 观念艺术（索尔·勒维特）
- 激浪派、贫困艺术、系统艺术
- 罗西·布拉伊多蒂的"后人类"
- 哈尔·福斯特的"归档冲动"

### 媒介与技术哲学
- 弗里德里希·基特勒的媒介决定论
- 吉尔伯特·西蒙东的"具体化"
- 贝尔纳·斯蒂格勒的"技术作为药理学"
- 弗卢塞尔的"技术图像"

### 相关运动
- 慢媒体运动
- 自愿简单主义
- 故障艺术（Glitch Art）
- 反设计

---

## 许可证

- **内容**: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)
- **代码**: [MIT License](LICENSE)

---

## 联系方式

- 🌐 **项目主页**: https://ewanqian.github.io/less-media-art
- 💻 **GitHub 仓库**: https://github.com/ewanqian/less-media-art
- 🐛 **问题反馈**: [GitHub Issues](https://github.com/ewanqian/less-media-art/issues)
- 💬 **讨论区**: [GitHub Discussions](https://github.com/ewanqian/less-media-art/discussions)

---

## 致谢

感谢所有为这个研究框架贡献思想、实践和代码的共同研究者们。

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
