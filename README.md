1. What is Pandas

Pandas is a Python library used for data analysis and data manipulation

Built on top of NumPy

Best for CSV, Excel, JSON, SQL data handling

2. Why Pandas is Used

Easy handling of large datasets

Fast data cleaning and preprocessing

Powerful functions for filtering, grouping, merging

Widely used in Data Science, ML, Analytics

3. Core Data Structures
a) Series

One-dimensional data structure

Similar to a column in a table

Can store different data types

Example:

[10, 20, 30, 40]

b) DataFrame

Two-dimensional (rows and columns)

Like an Excel sheet or SQL table

Most commonly used structure

4. Creating DataFrame

From list

From dictionary

From CSV / Excel / JSON

From NumPy array

5. Reading Files in Pandas

read_csv() → CSV file

read_excel() → Excel file

read_json() → JSON file

read_sql() → Database

6. Viewing Data

head() → First 5 rows

tail() → Last 5 rows

shape → Rows & columns count

info() → Data types & null values

describe() → Statistical summary

7. Data Selection

Column selection using column name

Row selection using index

Conditional filtering using conditions

8. Handling Missing Data

Missing values represented as NaN

Methods:

isnull()

notnull()

dropna()

fillna()

9. Handling Duplicate Data

duplicated() → find duplicates

drop_duplicates() → remove duplicates

10. Data Cleaning

Removing null values

Fixing wrong data types

Removing duplicates

Handling outliers

Formatting dates

11. Data Sorting

sort_values() → sort by column

sort_index() → sort by index

12. Grouping Data

groupby() used for:

sum

mean

count

min / max

Used mostly for analysis

13. Merging & Joining

merge() → SQL-like join

concat() → combine datasets

Join types:

inner

left

right

outer

14. Data Type Conversion

astype() → change data type

to_datetime() → convert to date format

15. Pandas with CSV (Real-World Use)

Import raw CSV

Clean dirty data

Analyze data

Export clean CSV

16. Advantages of Pandas

Easy syntax

Fast performance

Strong community support

Integrates with NumPy, Matplotlib, Seaborn

17. Limitations

Not ideal for very large big-data systems

High memory usage compared to databases

18. Pandas Use Cases

Data cleaning

Data preprocessing

Exploratory Data Analysis (EDA)

Machine Learning data preparation

Report generation
