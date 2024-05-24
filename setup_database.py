from pymongo import MongoClient
import pandas as pd
import os
import warnings

# Suppress specific openpyxl warnings
warnings.filterwarnings("ignore", category=UserWarning, module='openpyxl')

# Connect to MongoDB
client = MongoClient('localhost', 27017)
db = client['sikorsky_archives']

def normalize_date(date_str):
    """Normalize date to month/day/year format."""
    try:
        date_obj = pd.to_datetime(date_str, errors='coerce')
        if pd.isna(date_obj):
            return None
        return date_obj.strftime('%m/%d/%Y')
    except Exception as e:
        print(f"Error parsing date: {date_str} - {e}")
        return None

def process_aircraft_model(model_str):
    """Split aircraft model string into a list if it contains multiple values."""
    if isinstance(model_str, str):
        return [model.strip() for model in model_str.split(',')]
    return [model_str]

def preprocess_comments(comments):
    """Preprocess comments if needed."""
    if isinstance(comments, str):
        return comments.strip()
    return comments

def handle_nan_values(row):
    """Replace NaN values with None."""
    return {key: (value if pd.notna(value) else None) for key, value in row.items()}

def validate_data(row):
    """Validate and clean the data row by row."""
    row = handle_nan_values(row)

    # Validate Date format
    row['Date'] = normalize_date(row.get('Date'))

    # Normalize Aircraft_Model
    row['Aircraft_Model'] = process_aircraft_model(row.get('Aircraft_Model', None))

    # Preprocess comments
    row['Comment'] = preprocess_comments(row.get('Comment', ''))

    return row

def process_excel_file(file_path, collection_name):
    try:
        df = pd.read_excel(file_path)

        # Prepare documents for MongoDB
        documents = []
        for _, row in df.iterrows():
            cleaned_row = validate_data(row)
            document = {
                "searchTags": [cleaned_row.get('Search_1', ''), cleaned_row.get('Search_2', '')],
                "itemNumber": cleaned_row.get('Item_Number', ''),
                "indexes": {
                    "index1": cleaned_row.get('Index_1', ''),
                    "index2": cleaned_row.get('Index_2', 0)
                },
                "type": cleaned_row.get('Type', 'Unknown'),
                "reference": cleaned_row.get('Reference', 'N/A'),
                "fileLink": cleaned_row.get('See_It', 'No link provided'),
                "aircraftModel": cleaned_row.get('Aircraft_Model', 'Unknown'),
                "description": cleaned_row.get('Description', 'No description provided'),
                "names": cleaned_row.get('Names', 'Anonymous'),
                "date": cleaned_row.get('Date'),
                "comments": cleaned_row.get('Comment', '')
            }
            documents.append(document)

        # Insert documents into MongoDB
        if documents:
            db[collection_name].insert_many(documents)
            print(f"Inserted data from {file_path} into {collection_name} collection")
        else:
            print(f"No valid data found in {file_path}")
    except Exception as e:
        print(f"Failed to process {file_path}: {e}")

def main(root_directory):
    try:
        for root, dirs, files in os.walk(root_directory):
            # Process only the main folders (i.e., folders in root_directory)
            if root == root_directory:
                for dir_name in dirs:
                    dir_path = os.path.join(root_directory, dir_name)
                    print(f"Processing directory: {dir_path}")
                    # Only process files directly in this directory
                    for file in os.listdir(dir_path):
                        file_path = os.path.join(dir_path, file)
                        if os.path.isfile(file_path) and (file.endswith('.xls') or file.endswith('.xlsx')):
                            print(f"Processing file: {file_path}")
                            process_excel_file(file_path, dir_name)
                    print(f"Finished processing directory: {dir_path}")
                # Stop after processing the first level of directories
                break
    except Exception as e:
        print(f"Failed to process directory: {e}")

if __name__ == "__main__":
    main(r'E:\\Hank Sample File - Copy\DATABASE PROJECT\DOWNLOAD FILES')  # Use raw string for the path
