import logging
from config import *
import ocrmypdf 
from pathlib import Path

# This both serves as a test of the file links in the revised fileLink.py for the purposes of outputting PDFs (that are specifically not already OCR'd) into a local Output folder. 
# This currently does not write new these new file links to MongoDB, but very well could.

def ocr_all_blank_pdfs():
    pdf_directories = []
    for collection_name in collection_names:
        logging.info(f"Processing collection: {collection_name}")
        collection = db[collection_name]
        for document in collection.find():
            filename = document.get('fileLink')
            if (filename != 'None') and ('.pdf' in filename):
                print(filename)
                pdf_directories.append(filename)
    return pdf_directories

def create_ocr(all_pdfs):
    for x in all_pdfs:
        path = Path(x)
        try: 
            ocrmypdf.ocr(f'{x}', f'./Output/{path.name}')
        except: 
            print("Prior OCR found. Skipping...")

all_pdfs = ocr_all_blank_pdfs()

create_ocr(all_pdfs)
