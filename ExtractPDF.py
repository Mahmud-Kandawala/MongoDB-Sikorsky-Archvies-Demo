import fitz  # PyMuPDF ##
from pymongo import MongoClient

# Connect to the MongoDB server
client = MongoClient('mongodb://localhost:27017/')
db = client['sikorsky_archives']
collection = db['T01.10 Handouts']

# Function to extract text from a PDF file
def extract_text_from_pdf(file_path):
    try:
        doc = fitz.open(file_path)
        text = ""
        for page in doc:
            text += page.get_text()
        return text
    except Exception as e:
        print(f"Error extracting text from {file_path}: {e}")
        return ""

# Update documents with extracted text
for document in collection.find():
    file_path = document.get('fileLink')
    if file_path and file_path.endswith('.pdf'):
        extracted_text = extract_text_from_pdf(file_path)
        collection.update_one(
            {'_id': document['_id']},
            {'$set': {'extractedText': extracted_text}}
        )
        print(f"Updated document ID {document['_id']} with extracted text.")

# Close the connection to MongoDB
client.close()