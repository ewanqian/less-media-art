#!/usr/bin/env python3
"""
少媒体艺术网站生成器
将 Markdown 转换为静态 HTML
"""

import markdown
import os
import re
from pathlib import Path
from datetime import datetime

# 配置
DOCS_DIR = Path("../docs")
PUBLIC_DIR = Path("../Public")
TEMPLATE_DIR = Path("templates")

# Markdown 扩展
MD_EXTENSIONS = [
    'meta',
    'tables',
    'fenced_code',
    'toc',
    'footnotes',
]

# HTML 模板
PAGE_TEMPLATE = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | 少媒体艺术</title>
  <meta name="description" content="{description}">
  <link rel="stylesheet" href="{css_path}assets/css/style.css">
</head>
<body>
  <div class="container">
    <header class="site-header">
      <h1 class="site-title"><a href="{root_path}">少媒体艺术</a></h1>
      <p class="site-subtitle">Less-Media Art · 一个开放的研究框架</p>
      <nav class="site-nav">
        <ul>
          <li><a href="{root_path}">索引</a></li>
          <li><a href="{theory_path}theory/">理论</a></li>
          <li><a href="{methods_path}methods/">方法</a></li>
          <li><a href="{archive_path}archive/">档案</a></li>
          <li><a href="{discussion_path}discussion/">讨论</a></li>
          <li><a href="{about_path}about/">关于</a></li>
        </ul>
      </nav>
    </header>

    <main class="content">
      {breadcrumb}
      {content}
      
      <div class="related">
        <h3>相关页面</h3>
        <ul>
          {related_links}
        </ul>
      </div>
    </main>

    <footer class="site-footer">
      <p>
        少媒体艺术 · 开放研究框架<br>
        <a href="https://github.com/ewanqian/less-media-art">GitHub</a> · 
        内容遵循 <a href="https://creativecommons.org/licenses/by-sa/4.0/">CC BY-SA 4.0</a><br>
        <small>最后更新: {update_time}</small>
      </p>
    </footer>
  </div>
</body>
</html>
'''


def get_relative_paths(depth):
    """根据文件深度生成相对路径"""
    if depth == 0:
        return "", "", "", "", "", ""
    prefix = "../" * depth
    return prefix, prefix, prefix, prefix, prefix, prefix


def generate_breadcrumb(file_path, depth):
    """生成面包屑导航"""
    if depth == 0:
        return ""
    
    parts = file_path.parent.parts[2:]  # 去掉 docs/
    breadcrumb = '<nav class="breadcrumb">\n'
    breadcrumb += f'<a href="{ "../" * depth }">索引</a>'
    
    current_path = ""
    for i, part in enumerate(parts):
        current_path += "../" * (depth - i - 1) if i < depth - 1 else ""
        breadcrumb += f'\n<span class="separator">/</span>\n'
        breadcrumb += f'<a href="{current_path}{part}/">{part}</a>'
    
    breadcrumb += f'\n<span class="separator">/</span>\n<span>{file_path.stem}</span>'
    breadcrumb += '\n</nav>\n'
    return breadcrumb


def process_markdown(md_file):
    """处理单个 Markdown 文件"""
    with open(md_file, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    # 转换 Markdown
    md = markdown.Markdown(extensions=MD_EXTENSIONS)
    html_content = md.convert(md_content)
    
    # 获取元数据
    meta = md.Meta if hasattr(md, 'Meta') else {}
    title = meta.get('title', [md_file.stem])[0] if meta else md_file.stem
    description = meta.get('description', [''])[0] if meta else ''
    
    return html_content, title, description


def generate_related_links(file_path, depth):
    """生成相关链接"""
    prefix = "../" * depth
    links = [
        f'<li><a href="{prefix}theory/">理论词条总览</a> — 探索核心概念</li>',
        f'<li><a href="{prefix}methods/">方法工具箱</a> — 开始实践</li>',
        f'<li><a href="https://github.com/ewanqian/less-media-art">GitHub 仓库</a> — 参与贡献</li>',
    ]
    return '\n'.join(links)


def build_site():
    """构建整个网站"""
    print("开始构建少媒体艺术网站...")
    
    # 确保 Public 目录存在
    PUBLIC_DIR.mkdir(parents=True, exist_ok=True)
    
    # 复制 CSS
    css_source = Path("assets/css/style.css")
    css_target = PUBLIC_DIR / "assets" / "css" / "style.css"
    css_target.parent.mkdir(parents=True, exist_ok=True)
    if css_source.exists():
        import shutil
        shutil.copy2(css_source, css_target)
        print(f"✓ 复制 CSS: {css_target}")
    
    # 遍历所有 Markdown 文件
    md_files = list(DOCS_DIR.rglob("*.md"))
    print(f"找到 {len(md_files)} 个 Markdown 文件")
    
    for md_file in md_files:
        # 计算相对深度
        relative_path = md_file.relative_to(DOCS_DIR)
        depth = len(relative_path.parts) - 1
        
        # 处理 Markdown
        content, title, description = process_markdown(md_file)
        
        # 生成路径
        root_path, theory_path, methods_path, archive_path, discussion_path, about_path = get_relative_paths(depth)
        
        # 生成面包屑
        breadcrumb = generate_breadcrumb(relative_path, depth)
        
        # 生成相关链接
        related_links = generate_related_links(relative_path, depth)
        
        # 生成 HTML
        html = PAGE_TEMPLATE.format(
            title=title,
            description=description,
            css_path=root_path,
            root_path=root_path,
            theory_path=theory_path,
            methods_path=methods_path,
            archive_path=archive_path,
            discussion_path=discussion_path,
            about_path=about_path,
            breadcrumb=breadcrumb,
            content=content,
            related_links=related_links,
            update_time=datetime.now().strftime("%Y-%m-%d")
        )
        
        # 确定输出路径
        if md_file.name == "index.md":
            output_file = PUBLIC_DIR / relative_path.parent / "index.html"
        else:
            output_file = PUBLIC_DIR / relative_path.with_suffix(".html")
        
        output_file.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html)
        
        print(f"✓ 生成: {output_file}")
    
    print(f"\n构建完成！输出目录: {PUBLIC_DIR.absolute()}")


if __name__ == "__main__":
    build_site()
