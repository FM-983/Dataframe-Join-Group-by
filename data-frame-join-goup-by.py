"""
Class Exercise - Dataframe Join & Group by
Instructions:
Use the attached Dataframes and implement the following
"""
import numpy as np
import pandas as pd

products_df = pd.DataFrame({
    'Product_ID': [1, 2, 3],
    'Product_Name': ['iPhone 12', 'Samsung S21', 'Pixel 5'],
    'Product_Price': [999, 899, 699],
})
sales_df = pd.DataFrame({
    'Sale_ID': [1, 2, 3, 4, 5, 6, 7],
    'Sale_Date': pd.to_datetime(['2021-01-01', '2021-02-01', '2021-02-15', '2020-03-01', '2020-04-01',
    '2020-02-15', '2020-01-01']),
    'Customer_ID': [1, 2, 3, 2, 3, 4, 4],
    'Product_ID': [1, 1, 2, 2, 3, 3, 1],
})
customers_df = pd.DataFrame({
    'Customer_ID': [1, 2, 3, 4],
    'Customer_Name': ['John Doe', 'Jane Doe', 'Jim Brown', 'Jake Smith'],
    'Customer_Age': [25, 30, 35, 20],
    'Customer_Email': ['john@doe.com', 'jane@doe.com', 'jim@brown.com', 'jake@smith.com'],
})


"""
1) For each product calculate the number of customers that bought it and their average age
For example → For product ‘iPhone’ customer count was: 2 and average customer age was: 25
"""

sales_customers_df = pd.merge(sales_df, customers_df, on='Customer_ID')

product_sales_df = pd.merge(sales_customers_df, products_df, on='Product_ID')

product_customer_stats = product_sales_df.groupby('Product_Name').agg(
    Customer_Count=('Customer_ID', 'nunique'),
    Average_Age=('Customer_Age', 'mean')
).reset_index()
print(f"1)\n{product_customer_stats}\n")

"""
2) For each year calculate the total sales for each product for that year
For example → For year ‘2020’, for product ‘iPhone’ the number of sales was 1
"""

product_sales_df['Sale_Year'] = product_sales_df['Sale_Date'].dt.year

sales_by_year_product = product_sales_df.groupby(['Sale_Year', 'Product_Name']).size().reset_index(name='Total_Sales')
pivot_table = sales_by_year_product.pivot(index='Sale_Year', columns='Product_Name', values='Total_Sales').fillna(0)
print(f"2)\n{pivot_table}\n")
