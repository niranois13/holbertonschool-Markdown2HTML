#!/usr/bin/python3
"""Function to convert MarkDown into HTML"""
import sys
import os


def list_handler(lines):
    """
    Function helper to handle the parsing of lists
    :params lines: str - lines of a markdown file after a list marker ("- ")
    Returns: markdown list processed as HTML unordered lists,
            rest of the file and a list count to continue parsing
            """
    html_list = ["<ul>"]
    line_count = 0
    for line in lines:
        if line.startswith('- '):
            html_list.append(f"<li>{line[2:]}</li>")
            line_count += 1
        else:
            break
    html_list.append('</ul>')

    return html_list, line_count


def markdown2html(markdown_content):
    """
    Function used to convert Markdown text into HTML file
    :params markdown_text: str - the content to be converted
    Returns: the output content
    """
    html_lines = []
    lines = markdown_content.splitlines()
    i = 0

    while i < len(lines):
        line = lines[i]
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
        elif line.startswith("- "):
            list_html, line_count = list_handler(lines[i:])
            html_lines.extend(list_html)
            i += line_count
        i += 1

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
