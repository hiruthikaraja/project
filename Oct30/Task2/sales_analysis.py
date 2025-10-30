import pandas as pd
import numpy as np

# Load CSV
df = pd.read_csv("Sales.csv")

# Clean missing values
df.fillna(0, inplace=True)

# Format date
df['sale_date'] = pd.to_datetime(df['sale_date'])
df['month'] = df['sale_date'].dt.month

# Calculate inventory turnover
df['inventory_turnover'] = df['quantity'] / (df['quantity'].mean())

# Monthly sales summary
monthly_sales = df.groupby('month')['total_amount'].sum().reset_index()

# Top 5 best sellers
top_sellers = df.groupby('name')['total_amount'].sum().sort_values(ascending=False).head(5)

# Export processed file
df.to_csv("Processed_Sales.csv", index=False)
print("Processed dataset saved successfully.")
