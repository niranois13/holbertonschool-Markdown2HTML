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

    if not os.path.exists(markdown_file):
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)

    sys.exit(0)

if __name__ == "__main__":
    main()
