#!/usr/bin/env python3
import os
from PyPDF2 import PdfMerger

def concat_pdfs(output_path='chap23.pdf'):
    """
    Concatenate chapter 23 PDFs (English and Japanese versions)
    into a single PDF file.
    
    Args:
        output_path (str): Path for the output PDF file
    
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        # Input PDF files
        input_files = [
            'chap23_ja.md.pdf',
            'chap23_en.md.pdf',
        ]
        
        # Check if input files exist
        for file in input_files:
            if not os.path.exists(file):
                print(f"Error: {file} not found")
                return False
        
        # Create PDF merger object
        merger = PdfMerger()
        
        # Add each PDF to the merger
        for pdf in input_files:
            merger.append(pdf)
        
        # Write the merged PDF to output file
        merger.write(output_path)
        merger.close()
        
        print(f"Successfully created {output_path}")
        return True
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return False

if __name__ == "__main__":
    concat_pdfs()