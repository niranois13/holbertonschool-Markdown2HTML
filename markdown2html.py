#!/usr/bin/python3
import sys
import os

def main():
    """
    Function to convert markdown into HTML
    :params argv[1]: markdown entrypoint file name
    :params argv[2]: output file name
    Returns: 0 on success, 1 if markdown file doesn't exists or on missing argument"""
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)

    markdown_file = sys.argv[1]
    output_file = sys.argv[2]

    if not os.path.exists(markdown_file):
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)

    try:
        with open(markdown_file, "r", encoding="utf-8") as md_file:
            markdown_content = md_file.read()
    except Exception as e:
        print(f"Error reading {markdown_file}: {e}", file=sys.stderr)
        sys.exit(1)

    try:
        with open(output_file, "w", encoding="utf-8") as html_file:
            html_file.write(markdown_content)
    except Exception as e:
        print(f"Error writing to {output_file}: {e}", file=sys.stderr)
        sys.exit(1)

    exit (0)

if __name__ == "__main__":
    main()
