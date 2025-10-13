# Import PySpark functions
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum as _sum, round as _round

spark = SparkSession.builder.appName("Retail_ETL").getOrCreate()

# ----- Upload cleaned data (simulate inline here) -----
products_df = spark.createDataFrame([
    ("P001", "Laptop", "Electronics", 45000),
    ("P002", "Mobile", "Electronics", 15000),
    ("P003", "Book", "Stationery", 300),
    ("P004", "Headphones", "Accessories", 2000)
], ["product_id", "product_name", "category", "cost_price"])

sales_df = spark.createDataFrame([
    ("S001", "P001", 2, 55000),
    ("S002", "P002", 3, 25000),
    ("S003", "P003", 10, 700),
    ("S004", "P004", 5, 3000)
], ["sale_id", "product_id", "quantity", "sale_price"])

# ----- Transform and join -----
metrics_df = sales_df.join(products_df, "product_id", "inner") \
    .withColumn("total_sale", col("quantity") * col("sale_price")) \
    .withColumn("total_cost", col("quantity") * col("cost_price")) \
    .withColumn("profit", col("total_sale") - col("total_cost")) \
    .withColumn("profit_margin", _round((col("profit") / col("total_sale")) * 100, 2))

display(metrics_df)

# ----- Save final metrics -----
delta_path = "/mnt/retail360/etl/products_sales_metrics"
metrics_df.write.format("delta").mode("overwrite").save(delta_path)

csv_path = "/mnt/retail360/etl/products_sales_metrics_csv"
metrics_df.write.csv(csv_path, header=True, mode="overwrite")
