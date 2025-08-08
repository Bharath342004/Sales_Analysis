import pandas as pd
import matplotlib.pyplot as plt
try:
    df = pd.read_csv("sales.csv")
    print("CSV File Loaded Successfully")
except FileNotFoundError:
    print("CSV file not found. Please check the file name and path.")
    exit()
print("\nFirst 5 Rows of Data:\n", df.head())
print("\nShape of Data:", df.shape)
print("\nData Types:\n", df.dtypes)
print("\nMissing Values:\n", df.isnull().sum())
df = df.fillna(0)
print("\nSummary Statistics:\n", df.describe())
if "Region" in df.columns and "Sales" in df.columns:
    sales_by_region = df.groupby("Region")["Sales"].sum().sort_values(ascending=False)
    print("\nTotal Sales by Region:\n", sales_by_region)
    plt.figure(figsize=(8, 5))
    sales_by_region.plot(kind="bar", color="skyblue", edgecolor="black")
    plt.title("Total Sales by Region", fontsize=14)
    plt.xlabel("Region")
    plt.ylabel("Total Sales")
    for i, val in enumerate(sales_by_region):
        plt.text(i, val, str(val), ha='center', va='bottom', fontsize=9)
    plt.tight_layout()
    plt.show()
    sales_by_region.plot(kind="pie", autopct='%1.1f%%', figsize=(6, 6), startangle=90)
    plt.title("Sales Distribution by Region")
    plt.ylabel("")
    plt.show()
if "Month" in df.columns and "Sales" in df.columns:
    monthly_sales = df.groupby("Month")["Sales"].sum()
    print("\nMonthly Sales:\n", monthly_sales)

    plt.figure(figsize=(8, 5))
    monthly_sales.plot(kind="line", marker="o", color="green")
    plt.title("Monthly Sales Trend", fontsize=14)
    plt.xlabel("Month")
    plt.ylabel("Total Sales")
    for i, val in enumerate(monthly_sales):
        plt.text(i, val, str(val), ha='center', va='bottom', fontsize=9)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

df.to_csv("processed_sales.csv", index=False)
print("Processed data saved as 'processed_sales.csv'")
