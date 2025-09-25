import pandas as pd
import numpy as np

# Load CSV data
products = pd.read_csv('products.csv')
sales = pd.read_csv('sales.csv')

# Fill missing values and correct data types
products.fillna({'stock_quantity': 0, 'price': 0}, inplace=True)
sales.fillna({'quantity': 0, 'total_amount': 0}, inplace=True)
products['price'] = products['price'].astype(float)
sales['quantity'] = sales['quantity'].astype(int)
sales['total_amount'] = sales['total_amount'].astype(float)

# Merge datasets
merged = sales.merge(products, on='product_id', how='left')

# Calculate fields
merged['revenue'] = merged['quantity'] * merged['price']
merged['discount_percent'] = np.where(merged['category'] == 'Electronics', 10, 5)
merged['cost'] = merged['price'] * 0.6
merged['profit'] = merged['revenue'] - (merged['quantity'] * merged['cost'])
merged['profit_margin_%'] = (merged['profit'] / merged['revenue']) * 100

# Summaries
product_summary = merged.groupby('product_name')['revenue'].sum()
store_summary = merged.groupby('store_id')['revenue'].sum()

# Display results
print(merged[['sale_id', 'product_name', 'store_id', 'quantity', 'price', 'revenue', 'profit', 'profit_margin_%']])
print(product_summary)
print(store_summary)

# Save cleaned data
merged.to_csv('cleaned_sales_data.csv', index=False)
