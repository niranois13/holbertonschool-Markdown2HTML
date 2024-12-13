#!/usr/bin/python3
"""Function to convert MarkDown into HTML"""
import sys
import os


def paragraph_handler(lines):
    """
    Function helper to handle the parsing of paragraphs
    :params lines: str - lines of a markdown file
                    starting with an alphanumeric character
    Returns: mardown paragraph processed as HTML <p>,
            rest of file and line_count to conitnue parsing
    """
    paragraph_lines = []
    line_count = 0

    for line in lines:
        if line.strip() == '':
            break
        if line_count > 0:
            paragraph_lines.append('<br/>')
        paragraph_lines.append(line)
        line_count += 1

    html_parag = ["<p>", *paragraph_lines, "</p>"]
    return html_parag, line_count


def ulist_handler(lines):
    """
    Function helper to handle the parsing of unordered lists
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


def olist_handler(lines):
    """
    Function helper to handle the parsing of ordered lists
    :params lines: str - lines of a markdown file after a list marker ("- ")
    Returns: markdown list processed as HTML ordered lists,
            rest of the file and a list count to continue parsing
    """
    html_list = ["<ol>"]
    line_count = 0
    for line in lines:
        if line.startswith('* '):
            html_list.append(f"<li>{line[2:]}</li>")
            line_count += 1
        else:
            break
    html_list.append('</ol>')

    return html_list, line_count


def b_formating(line):
    """
    Functon used to convert markdown bold syntax to the HTML one:
    **emphasis** into <b>emphasis</b>
    :params line: str - a line of the markdown to be pased for bold syntax
    Returns: the line string with the bold HTML syntax
    """
    formatted_line = []
    i = 0

    print(f'Input line: {line}')

    while i < len(line):
        if line[i:i+2] == '**' and line[i-1] != "\\":
            next_b_tag = line.find('**', i+2)
            if next_b_tag != -1:
                formatted_line.append('<b>')
                formatted_line.append(line[i+2:next_b_tag])
                formatted_line.append('</b>')
                i = next_b_tag + 2
            else:
                formatted_line.append(line[i])
                i += 1
        else:
            formatted_line.append(line[i])
            i += 1

    return "".join(formatted_line)


def em_formating(line):
    """
    Functon used to convert markdown emphasis syntax to the HTML one:
    __emphasis__ into <em>emphasis</em>
    :params line: str - a line of the markdown to be pased for emphasis syntax
    Returns: the line string with te HTML syntax for emphasis
    """
    formatted_line = []
    i = 0

    while i < len(line):
        if line[i] == '_' and line[i-1] != "\\":
            next_em_tag = line.find('_', i+1)
            if next_em_tag != -1:
                formatted_line.append('<em>')
                formatted_line.append(line[i+1:next_em_tag])
                formatted_line.append('</em>')
                i = next_em_tag + 1
            else:
                formatted_line.append(line[i])
                i += 1
        else:
            formatted_line.append(line[i])
            i += 1

    return "".join(formatted_line)


def markdown2html(markdown_content):
    """
    Function used to convert Markdown text into HTML file
    :params markdown_text: str - the content to be converted
    Returns: the output content
    """
    html_lines = []
    lines = markdown_content.splitlines()
    b_formatted_lines = [b_formating(line) for line in lines]
    formatted_lines = [em_formating(line) for line in b_formatted_lines]
    i = 0

    while i < len(formatted_lines):
        line = formatted_lines[i]
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
            list_html, line_count = ulist_handler(formatted_lines[i:])
            html_lines.extend(list_html)
            i += line_count
            continue
        elif line.startswith("* "):
            list_html, line_count = olist_handler(formatted_lines[i:])
            html_lines.extend(list_html)
            i += line_count
            continue
        elif line.strip() and not line.startswith(('# ', '- ', '* ')):
            paragraph_html, line_count = paragraph_handler(formatted_lines[i:])
            html_lines.extend(paragraph_html)
            i += line_count
            continue
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
