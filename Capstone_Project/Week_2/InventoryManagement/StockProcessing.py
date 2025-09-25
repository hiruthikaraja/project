# Week 3 - Warehouse-Level Stock Insights (PySpark)
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when, sum as spark_sum

# Initialize Spark
spark = SparkSession.builder.appName("WarehouseStockInsights").getOrCreate()

# Load Stock Movements CSV
df = spark.read.csv("stock_movements_warehouse.csv", header=True, inferSchema=True)

# Transform Data
df = df.withColumn("movement_type", col("movement_type").upper())
df = df.withColumn("net_quantity",
                   when(col("movement_type") == "IN", col("quantity"))
                   .when(col("movement_type") == "OUT", -col("quantity"))
                   .otherwise(col("quantity")))

# Aggregate Stock per Warehouse
warehouse_stock = df.groupBy("warehouse_id", "warehouse_name") \
    .agg(
        spark_sum("net_quantity").alias("total_stock"),
        spark_sum("reorder_level").alias("total_reorder"),
        spark_sum("capacity").alias("total_capacity")
    )

# Identify Overstocked / Understocked Warehouses
warehouse_status = warehouse_stock.withColumn(
    "status",
    when(col("total_stock") > col("total_capacity") * 0.9, "OVERSTOCKED")
    .when(col("total_stock") < col("total_reorder"), "UNDERSTOCKED")
    .otherwise("NORMAL")
)

# Show Results
warehouse_status.show(truncate=False)

# Save Results
warehouse_status.coalesce(1).write.csv("warehouse_stock_status.csv", header=True, mode="overwrite")

spark.stop()
