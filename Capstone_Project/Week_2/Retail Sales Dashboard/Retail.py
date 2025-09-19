import pandas as pd
import numpy as np

# Load CSV data
products = pd.read_csv('products.csv')
sales = pd.read_csv('sales.csv')

# Data Cleaning

# Handle missing values
products.fillna({'stock_quantity': 0, 'price': 0}, inplace=True)
sales.fillna({'quantity': 0, 'total_amount': 0}, inplace=True)

# Convert data types
products['price'] = products['price'].astype(float)
sales['quantity'] = sales['quantity'].astype(int)
sales['total_amount'] = sales['total_amount'].astype(float)


# Merge both datasets

merged = sales.merge(products, on='product_id', how='left')

# Calculate new fields

# Revenue = quantity * price
merged['revenue'] = merged['quantity'] * merged['price']

# Assume discount 10% on Electronics, 5% on others
merged['discount_percent'] = np.where(
    merged['category'] == 'Electronics', 10, 5
)

# Profit = revenue - (cost = price * 0.6 assumed as cost)
merged['cost'] = merged['price'] * 0.6
merged['profit'] = merged['revenue'] - (merged['quantity'] * merged['cost'])

# Profit Margin %
merged['profit_margin_%'] = (merged['profit'] / merged['revenue']) * 100

# Grouped summaries

# Total revenue by product
product_summary = merged.groupby('product_name')['revenue'].sum()

# Total revenue by store
store_summary = merged.groupby('store_id')['revenue'].sum()


# Print Results

print("\n==== Cleaned Merged Dataset ====")
print(merged[['sale_id', 'product_name', 'store_id', 'quantity',
              'price', 'revenue', 'profit', 'profit_margin_%']])

print("\n==== Total Revenue by Product ====")
print(product_summary)

print("\n==== Total Revenue by Store ====")
print(store_summary)

# Save cleaned data back to CSV
merged.to_csv('cleaned_sales_data.csv', index=False)
print("\n✅ Cleaned data saved as cleaned_sales_data.csv")
