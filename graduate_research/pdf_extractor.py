import PyPDF2
import re
import pandas as pd
from pathlib import Path

def extract_text_from_pdf(pdf_path):
    """Extract text from PDF file"""
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page in reader.pages:
            text += page.extract_text()
    return text

def find_hiring_numbers(text):
    """Find mentions of new graduate hiring numbers in text"""
    # Common patterns in Japanese annual reports for new graduate hiring
    patterns = [
        r'新卒採用[^\d]*(\d+)[名人]',
        r'新卒[^\d]*(\d+)[名人]を採用',
        r'新卒社員[^\d]*(\d+)[名人]',
        r'新卒入社[^\d]*(\d+)[名人]'
    ]
    
    for pattern in patterns:
        matches = re.finditer(pattern, text)
        for match in matches:
            return int(match.group(1))
    return None

def process_rakuten_reports():
    """Process Rakuten annual reports and extract hiring data"""
    data = []
    pdf_dir = Path('.')
    
    # Process each PDF file
    for pdf_file in pdf_dir.glob('rakuten_*.pdf'):
        year = int(pdf_file.stem.split('_')[1])
        text = extract_text_from_pdf(pdf_file)
        hiring_number = find_hiring_numbers(text)
        
        if hiring_number:
            data.append({
                'company': 'Rakuten',
                'year': year,
                'new_grads_hired': hiring_number,
                'notes': 'Extracted from annual report'
            })
        else:
            print(f"Could not find hiring numbers in {pdf_file}")
    
    return pd.DataFrame(data)

if __name__ == '__main__':
    # Install required packages
    import subprocess
    subprocess.run(['pip', 'install', 'PyPDF2', 'pandas'])
    
    # Process Rakuten reports
    df = process_rakuten_reports()
    print("\nExtracted Data:")
    print(df)
    
    # Save intermediate results
    df.to_csv('rakuten_hiring_data.csv', index=False)
    print("\nData saved to rakuten_hiring_data.csv")
