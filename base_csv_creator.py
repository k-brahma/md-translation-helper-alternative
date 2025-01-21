"""
read chap23_en.md's each line and create base_csv.csv with format:

english,japanese
line1,line1
line2,line2
...

Empty lines are skipped.
"""

import csv
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def read_md_file():
    """Read markdown file using BASE_DIR"""
    md_path = os.path.join(BASE_DIR, 'chap23_en.md')
    with open(md_path, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]
    return lines


def create_csv(lines):
    """Create CSV file with headers using BASE_DIR"""
    csv_path = os.path.join(BASE_DIR, 'base_csv.csv')
    with open(csv_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        # Write header
        writer.writerow(['english', 'japanese'])
        # Write content
        for line in lines:
            writer.writerow([line, line])
    return


def main():
    lines = read_md_file()
    create_csv(lines)
    print(f"Created CSV with {len(lines)} lines")
    return


if __name__ == '__main__':
    main()