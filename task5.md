# TASK 5

1. **What is Pandas used for?**  
Pandas is a **Python library** for **data cleaning, transformation, analysis, and visualization** in tabular form.

2. **What’s a DataFrame?**  
A **2D labeled data structure** with rows and columns, similar to an **Excel sheet** in Python.

3. **How do you read a CSV file?**  
import pandas as pd  
df = pd.read_csv("file.csv")  
Loads CSV data into a DataFrame.

4. **What is groupby()?**  
Used to **split data into groups** based on a column and then apply aggregation functions like sum() or mean().

5. **How do you filter rows?**  
df[df['Sales'] > 1000]  
Returns rows where Sales > 1000.

6. **Difference between loc[] and iloc[]?**  
loc[] → label-based selection (df.loc[2, 'Name'])  
iloc[] → index position-based (df.iloc[2, 1])

7. **What does .head() do?**  
Displays first 5 rows by default. Example: df.head(10)

8. **How can you create a bar chart?**  
df.plot(kind='bar')      # Pandas  
plt.bar(x, y)            # Matplotlib

9. **What’s the shape of a DataFrame?**  
df.shape  
Returns (rows, columns) tuple.

10. **What is NaN?**  
NaN stands for “Not a Number” – represents missing or undefined values in Pandas.
