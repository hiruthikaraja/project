"""
Week 2 - Stock Processing using Python
Tools: Pandas, NumPy
"""

import pandas as pd
import numpy as np

# Load CSV
df = pd.read_csv("stock_movements.csv")

#Clean Data
df['date'] = pd.to_datetime(df['date'], errors='coerce')   # clean dates
df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce').fillna(0).astype(int)
df['movement_type'] = df['movement_type'].str.upper().fillna('ADJUST')

# Convert IN/OUT to signed quantity
df['adjusted_qty'] = np.where(df['movement_type'] == 'IN',
                              df['quantity'],
                              np.where(df['movement_type'] == 'OUT',
                                       -df['quantity'],
                                       df['quantity']))

#  Calculate stock per product 
stock_summary = df.groupby(['product_id', 'product_name', 'reorder_level'], as_index=False)['adjusted_qty'].sum()
stock_summary.rename(columns={'adjusted_qty': 'current_stock'}, inplace=True)

# Flag low stock 
stock_summary['below_reorder'] = stock_summary['current_stock'] < stock_summary['reorder_level']

# Save reports
stock_summary.to_csv("stock_report.csv", index=False)
low_stock = stock_summary[stock_summary['below_reorder']]
low_stock.to_csv("low_stock_report.csv", index=False)

#Console Output 
print("\n📦 Stock Summary:")
print(stock_summary.to_string(index=False))

print("\n⚠️ Low Stock Items:")
print(low_stock.to_string(index=False))
