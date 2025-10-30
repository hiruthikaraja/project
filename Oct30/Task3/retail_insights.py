from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum as spark_sum

spark = SparkSession.builder.appName("RetailInsights").getOrCreate()

sales_df = spark.read.csv("Processed_Sales.csv", header=True, inferSchema=True)
inventory_df = spark.read.csv("inventory.csv", header=True, inferSchema=True)

# Join and aggregate
joined_df = sales_df.join(inventory_df, ["product_id"], "inner")
category_sales = joined_df.groupBy("category").agg(spark_sum("total_amount").alias("category_sales"))

# Export
category_sales.write.mode("overwrite").csv("/content/Average_Monthly_Revenue")

print("Category-wise sales by region saved.")
