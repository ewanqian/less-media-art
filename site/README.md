# 少媒体艺术网站生成器

将 Markdown 文档转换为静态 HTML 网站。

## 使用方法

### 本地构建

```bash
cd site
pip install markdown
python build.py
```

生成的网站位于 `../Public/` 目录。

### 本地预览

```bash
cd ../Public
python -m http.server 8000
```

访问 http://localhost:8000

## 工作原理

1. 读取 `../docs/` 目录下的所有 `.md` 文件
2. 使用 Python-Markdown 转换为 HTML
3. 应用 HTML 模板（包含导航、面包屑、页脚）
4. 输出到 `../Public/` 目录

## 文档格式

Markdown 文件支持 YAML Front Matter：

```markdown
---
title: 页面标题
description: 页面描述
---

# 正文内容
```

## 自动部署

GitHub Actions 工作流会在每次 push 到 main 分支时自动构建并部署到 GitHub Pages。
