"""
Convert chap23_en.md to chap23_ja.md using translations from base_csv.csv
Replace lines from longest to shortest to avoid partial matches.
"""

import csv
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def load_translations():
    """Load translations and sort by length of English text in descending order"""
    translations = []
    with open(os.path.join(BASE_DIR, 'translations.csv'), 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            eng = row['english'].strip()
            jpn = row['japanese'].strip()
            if eng and jpn:  # Skip empty entries
                translations.append((eng, jpn, len(eng)))
    
    # Sort by length in descending order
    return sorted(translations, key=lambda x: x[2], reverse=True)

def main():
    try:
        # Load translations
        translations = load_translations()
        
        # Read English content
        with open(os.path.join(BASE_DIR, 'chap23_en.md'), 'r', encoding='utf-8') as f:
            content = f.read()

        # Replace lines from longest to shortest
        for eng, jpn, _ in translations:
            # check if the line contains the English text
            if eng in content:
                content = content.replace(eng, jpn)
            else:
                print(f"Skipping: {eng}")
        
        # Save Japanese version
        with open(os.path.join(BASE_DIR, 'chap23_ja.md'), 'w', encoding='utf-8') as f:
            f.write(content)
            
        print("Conversion completed successfully!")
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()