#!/usr/bin/python3
"""Function to convert MarkDown into HTML"""
import sys
import os


def markdown2html(markdown_content):
    """
    Function used to convert Markdown text into HTML file
    :params markdown_text: str - the content to be converted
    Returns: the output content
    """
    html_lines = []
    for line in markdown_content.splitlines():
        if line.startswith("# "):
            html_lines.append(f"<h1>{line[2:]}</h1>")
        elif line.startswith("## "):
            html_lines.append(f"<h2>{line[3:]}</h2>")
        elif line.startswith("### "):
            html_lines.append(f"<h3>{line[4:]}</h3>")
        elif line.startswith("#### "):
            html_lines.append(f"<h4>{line[5:]}</h4>")
        elif line.startswith("##### "):
            html_lines.append(f"<h5>{line[6:]}</h5>")
        elif line.startswith("###### "):
            html_lines.append(f"<h6>{line[7:]}</h6>")
    return "\n".join(html_lines)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html",
              file=sys.stderr)
        sys.exit(1)

    markdown_file = sys.argv[1]
    output_file = sys.argv[2]

    if not os.path.exists(markdown_file):
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)

    try:
        with open(markdown_file, 'r', encoding='utf-8') as md_file:
            markdown_content = md_file.read()
    except Exception as e:
        print(f"Error reading {markdown_file}, {e}", file=sys.stderr)
        sys.exit(1)

    output_content = markdown2html(markdown_content)
    try:
        with open(output_file, "w", encoding="utf-8") as html_file:
            html_file.write(output_content)
    except Exception as e:
        print(f"Error writing to {output_file}, {e}", file=sys.stderr)
        sys.exit(1)

    sys.exit(0)
