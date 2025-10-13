from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when

# Create Spark session
spark = SparkSession.builder.appName("Inventory_ETL_Capstone").getOrCreate()

# Load cleaned stock data
stock_df = spark.createDataFrame([
    ("P001", "W001", 50, 20),
    ("P002", "W001", 10, 15),
    ("P003", "W002", 100, 30),
    ("P004", "W002", 5, 10)
], ["product_id", "warehouse_id", "quantity", "reorder_level"])

#Load cleaned product data
product_df = spark.createDataFrame([
    ("P001", "Laptop", "Electronics"),
    ("P002", "Mobile", "Electronics"),
    ("P003", "Book", "Stationery"),
    ("P004", "Headphones", "Accessories")
], ["product_id", "product_name", "category"])

#Join product and warehouse info
inventory_df = stock_df.join(product_df, "product_id", "inner")

#  Create master inventory view with reorder flag
inventory_df = inventory_df.withColumn(
    "reorder_flag",
    when(col("quantity") <= col("reorder_level"), "YES").otherwise("NO")
)

display(inventory_df)

# Save output in Delta and CSV formats
delta_path = "/mnt/retail360/inventory/master_inventory"
inventory_df.write.format("delta").mode("overwrite").save(delta_path)

csv_path = "/mnt/retail360/inventory/master_inventory_csv"
inventory_df.write.csv(csv_path, header=True, mode="overwrite")

print("Inventory ETL Completed: Delta & CSV saved")
