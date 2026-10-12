# Python API ETL Pipeline

A hands-on Data Engineering project that extracts data from a REST API, validates and transforms records, and loads clean data into a CSV file using Python.

## Project Overview

This project demonstrates the fundamentals of building a modular ETL pipeline using Python and the JSONPlaceholder REST API.

The pipeline separates extraction, transformation, and loading into reusable functions and includes basic error handling, logging, pagination, data quality checks, and safer file output.

## Architecture

REST API → Extract → Transform and Validate → Load → CSV Output

## Features

- **API extraction:** Retrieve JSON data using Python's `requests` library.
- **Pagination:** Fetch records across multiple API pages.
- **Data transformation:** Clean text fields and validate required fields.
- **Data quality:** Track extracted, accepted, and rejected records.
- **Error handling:** Handle HTTP, JSON parsing, and file-operation errors.
- **Logging:** Record pipeline progress and failures.
- **CSV output:** Write cleaned records using Python's built-in `csv` module.
- **Modular design:** Organize the workflow into reusable ETL functions.

## Technology Stack

- Python
- REST APIs
- Requests
- JSON
- CSV
- Python logging

## Project Structure

```text
python-api-etl-pipeline/
├── api_etl.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/python-api-etl-pipeline.git
cd python-api-etl-pipeline
```

Replace `YOUR_USERNAME` with your GitHub username.

### 2. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 3. Run the pipeline

```bash
python api_etl.py
```

The pipeline retrieves data from the API, applies transformation and validation rules, and writes the cleaned records to `cleaned_posts.csv`.

## Data Quality

The pipeline tracks:

- Total records extracted
- Records accepted after validation
- Records rejected during transformation

The expected reconciliation is:

`Extracted = Accepted + Rejected`

## What I Learned

Through this project, I practiced:

- Consuming REST APIs with Python
- Working with JSON data
- Cleaning and validating records
- Implementing pagination
- Handling errors and logging pipeline activity
- Writing structured CSV output
- Organizing an ETL workflow into reusable functions

## Future Improvements

- Add automated unit tests
- Implement duplicate detection
- Strengthen schema validation
- Add pipeline execution metrics
- Explore incremental data loading
- Containerize the application with Docker

## Data Source

[JSONPlaceholder](https://jsonplaceholder.typicode.com/) — a free fake REST API for testing and prototyping.

---

**Author:** Nadhiya Ganesan
