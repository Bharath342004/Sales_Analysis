# Sales Data Analysis

## Overview
This project analyzes sales data from a CSV file and generates:
- Sales by Region (Bar Chart)
- Monthly Sales Trend (Line Chart, if month data exists)
- Processed Sales File (`processed_sales.csv`)

---

## Project Structure
sales-analysis/
│
├── sales_analysis.py     # Main Python script
├── sales.csv             # Input sales data file
├── processed_sales.csv   # Output processed file (auto-generated after running script)
└── README.md             # Project documentation

---

## Requirements
Before running, install the required Python libraries:

pip install pandas matplotlib

---

## How to Run
1. Clone the Repository:
git clone https://github.com/yourusername/sales-analysis.git
cd sales-analysis

2. Place your sales.csv file in the project folder.
Example sales.csv:
Region,Month,Sales
East,Jan,1200
West,Jan,1500
East,Feb,1800
West,Feb,2000

3. Run the Script:
python sales_analysis.py

4. View Output:
- Charts will be displayed in a pop-up window.
- Processed Data will be saved as processed_sales.csv in the same folder.

---

## Sample Output
Sales by Region
Region
East    3000
West    3500

---

## Notes
- If your data does not contain a Month column, the monthly sales trend chart will be skipped.
- Make sure sales.csv has correct column names: Region, Month (optional), Sales.
