# Student Data Analysis System

A Python data analysis project that uses pandas, Excel and Matplotlib to analyse student academic performance and generate reports.

## Features

- Loads student records from an Excel spreadsheet.
- Cleans missing and invalid data.
- Calculates average, highest and lowest marks.
- Calculates the overall pass rate.
- Assigns performance categories:
  - Distinction: 75 and above
  - Pass: 50–74
  - Fail: Below 50
- Generates a text-based performance report.
- Creates a bar chart showing student marks.

## Technologies Used

- Python
- Pandas
- Matplotlib
- Excel
- OpenPyXL

## Project Files

| File | Description |
|---|---|
| `data_analysis.py` | Main Python analysis program |
| `students.xlsx` | Sample student dataset |
| `report.txt` | Generated performance report |
| `marks_chart.png` | Visual representation of student marks |
| `requirements.txt` | Required Python libraries |

## Installation

Install the required dependencies:

```bash
py -m pip install -r requirements.txt
```

## How to Run

Run the program from the project directory:

```bash
py data_analysis.py
```

Make sure `students.xlsx` is in the same directory as the Python script.

## Sample Results

- Average mark: 71.0
- Highest mark: 90
- Lowest mark: 50
- Pass rate: 100.0%

## Dataset

The project uses sample student names and academic marks for demonstration purposes. It does not contain real student records.

## Learning Outcomes

This project demonstrates practical use of Python, data cleaning, spreadsheet processing, calculations, data categorisation, report generation and data visualisation.
