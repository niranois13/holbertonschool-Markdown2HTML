#!/usr/bin/python3
import sys
import os

def main(markdown_file, output_file):
    """
    Function to convert markdown into HTML
    :params argv[1]: str - markdown entrypoint file name
    :params argv[2]: str - output file name
    Returns: 0 on success, 1 if markdown file doesn't exists or on missing argument"""

    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)

    if not os.path.exists(markdown_file):
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)

    sys.exit(0)

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
