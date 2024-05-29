import fitz  # PyMuPDF
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['sikorsky_archives']
handouts_collection = db['T01.10 Handouts']

def search_text_in_pdf(file_path, search_text):
    """Search for text in a PDF and return pages where it's found."""
    try:
        doc = fitz.open(file_path)
        results = []
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            text_instances = page.search_for(search_text)
            if text_instances:
                results.append(page_num + 1)  # Page numbers are 1-based
        return results
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return []

def search_text_in_handouts(search_text):
    """Search for text in all handouts PDFs and print results."""
    for document in handouts_collection.find({"fileLink": {"$regex": ".pdf$"}}):
        file_path = document.get('fileLink')
        if file_path:
            print(f"Searching in {file_path}...")
            pages = search_text_in_pdf(file_path, search_text)
            if pages:
                print(f"Text '{search_text}' found in {file_path} on pages: {pages}")
            else:
                print(f"Text '{search_text}' not found in {file_path}.")

if __name__ == '__main__':
    search_text = "New York"  # Replace with the text you're searching for
    search_text_in_handouts(search_text)
    client.close()
