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

