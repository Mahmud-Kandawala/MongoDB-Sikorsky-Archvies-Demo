# Sikorsky Archives MongoDB Demo

This project is a demonstration of how to process and import a large dataset of Excel files into MongoDB. The goal is to facilitate easy searching, updating, inserting, and retrieving of data for the Sikorsky Archives.

## Table of Contents

- [Project Overview](#project-overview)
- [Setup Instructions](#setup-instructions)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Script Details](#script-details)
  - [Key Functions](#key-functions)
- [Data Validation](#data-validation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

This project processes a dataset of approximately 40 GB, stored in various Excel files, and imports it into MongoDB. Each main folder in the dataset corresponds to a collection in MongoDB. Subfolders within these main folders are skipped.

## Setup Instructions

### Prerequisites

- Python 3.6+
- MongoDB Community Edition
- `pandas` library
- `pymongo` library
- `openpyxl` and `xlrd` libraries for handling Excel files

### Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/MongoDB-Sikorsky-Archives-Demo.git
   cd MongoDB-Sikorsky-Archives-Demo
2. **Install the Required Python Libraries:**
   ```bash
   pip install -r requirements.txt
3. **Set Up MongoDB:**
   - Ensure MongoDB is installed and running on your local machine.
   - The default connection string is mongodb://localhost:27017. Update this in the script if necessary.

## Script Details 
The script setup_database.py processes and imports Excel files into MongoDB. It handles both .xls and .xlsx file formats.

### Key Functions

- **normalize_date(date_str)**: Normalizes date formats to month/day/year.
- **process_aircraft_model(model_str)**: Splits aircraft model strings into lists.
- **preprocess_comments(comments)**: Preprocesses comments.
- **handle_nan_values(row)**: Replaces NaN values with None.
- **validate_data(row)**: Validates and cleans each data row.
- **process_excel_file(file_path, collection_name)**: Reads and processes an Excel file, then inserts data into MongoDB.
- **main(root_directory)**: Traverses the root directory, processing each main folder and its Excel files.

## Data Validation

The script includes data validation to ensure consistency:

- Dates are normalized to month/day/year.
- NaN values are replaced with None.
- Aircraft models with multiple values are split into lists.
- Comments are preprocessed to remove excess whitespace.

## Usage

1. **Ensure MongoDB is running:**
   ```bash
   mongod 
2. **Run the Script:**
   ```bash
   python setup_database.py /path/to/root_directory
3. **Script Output:**
The script logs each directory and file it processes.
It prints messages indicating successful insertion of data or any errors encountered.

## Contributing

Please follow these steps to contribute:

1. **Fork the Repository:**
   - Click the "Fork" button at the top right of the repository page.
2. **Clone Your Fork:**
   ```bash
   git clone https://github.com/yourusername/MongoDB-Sikorsky-Archives-Demo.git
   cd MongoDB-Sikorsky-Archives-Demo
3. **Create a New Branch:**
   ```bash
   git checkout -b feature/your-feature-name
4. **Make Your Changes and Commit:**
   ```bash
    git add .
    git commit -m "Add your commit message here"

5. **Push to Your Fork and Submit a Pull Request:**
   ```bash
    git push origin feature/your-feature-name

# License
This project is licensed under the MIT License. See the LICENSE file for details.

`This README is fully detailed and provides all necessary information for users and contributors, including a fully populated Table of Contents. If you need any more assistance, let me know! `
