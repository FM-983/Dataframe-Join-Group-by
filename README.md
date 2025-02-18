# Product Sales Analysis with Pandas

This repository contains a Python script that demonstrates data manipulation and analysis using the Pandas library. The script processes sales data, calculates customer statistics for each product, and determines yearly sales totals per product.

## Table of Contents

* [Introduction](#introduction)
* [Requirements](#requirements)
* [Usage](#usage)
* [DataFrames](#dataframes)
* [Calculations](#calculations)
* [Output](#output)

## Introduction

The script utilizes three Pandas DataFrames: `products_df`, `sales_df`, and `customers_df`.  It performs the following operations:

1.  Merges the DataFrames to create a comprehensive sales dataset.
2.  Calculates the number of customers who purchased each product and their average age.
3.  Calculates the total sales for each product for each year.

This analysis provides valuable insights into product performance and customer demographics.

## Requirements

*   Python 3
*   Pandas library: `pip install pandas`
*   NumPy library (already included with Pandas): `pip install numpy`

## Usage

1.  Clone the repository: `git clone https://github.com/FM-983/Dataframe-Join-Group-by.git` (or your repository URL)
2.  Navigate to the directory: `cd Dataframe-Join-Group-by`
3.  Run the script (e.g., if it's named `sales_analysis.py`): `python sales_analysis.py`

## DataFrames

The script initializes three DataFrames:

*   `products_df`: Contains information about each product (ID, name, price).
*   `sales_df`: Contains sales records (ID, date, customer ID, product ID).
*   `customers_df`: Contains customer information (ID, name, age, email).

## Calculations

The script performs the following calculations:

1.  **Merging DataFrames:**  Merges `sales_df` and `customers_df` based on `Customer_ID`, then merges the result with `products_df` based on `Product_ID`.
2.  **Customer Statistics:** Groups the merged DataFrame by `Product_Name` and calculates the number of unique customers (`Customer_Count`) and the average customer age (`Average_Age`).
3.  **Yearly Sales:** Extracts the year from the `Sale_Date`, groups the data by year and product, and calculates the total sales for each product in each year.  The results are then presented in a pivot table.

## Output

The script produces two output DataFrames:

1.  `product_customer_stats`: Shows the customer count and average age for each product.
2.  `pivot_table`: Shows the total sales for each product for each year.

These DataFrames are typically printed to the console.  You can modify the script to save them to files (e.g., CSV) if needed.  For example:

```python
product_customer_stats.to_csv("product_customer_stats.csv", index=False)
pivot_table.to_csv("yearly_sales.csv", index=False)
