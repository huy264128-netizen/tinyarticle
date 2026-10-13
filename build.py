#!/usr/bin/env python3
from pathlib import Path
import os
import markdown


def convert(file: Path):
    source = file.read_text(encoding="UTF-8")
    output = file.with_suffix(".html")
    title = file.name
    content = markdown.markdown(source,extensions=["extra","toc",])
    html = f"""<!DOCTYPE html>
    <html lang="zh-CN">
    <link rel="stylesheet"
          href="https://cdn.jsdelivr.net/npm/katex@0.16.22/dist/katex.min.css">

    <script defer
            src="https://cdn.jsdelivr.net/npm/katex@0.16.22/dist/katex.min.js"></script>

    <script defer
            src="https://cdn.jsdelivr.net/npm/katex@0.16.22/dist/contrib/auto-render.min.js"
            onload="renderMathInElement(document.body)"></script>
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{title}</title>
    </head>
    <body>
    <main>{content}</main>
    </body>
    </html>
    """
    output.write_text(html,encoding="UTF-8")
def main():
    for file in Path(".").rglob("*.md"):
        convert(file)
main()
