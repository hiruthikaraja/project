from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum as _sum, when

# Step 1: Start Spark session
spark = SparkSession.builder.appName("WarehouseStockInsights").getOrCreate()

# Step 2: Load stock movement data (CSV or JSON)
df = spark.read.csv("stockmovements.csv", header=True, inferSchema=True)

# Step 3: Clean & transform
df = df.withColumn("quantity", col("quantity").cast("int"))

# Step 4: Calculate net stock per warehouse & product
stock_summary = df.groupBy("warehouse_id", "product_id") \
    .agg(_sum("quantity").alias("total_stock"))

# Step 5: Load product reorder levels (from products.csv)
products = spark.read.csv("products.csv", header=True, inferSchema=True) \
    .select("product_id", "reorder_level")

# Join stock summary with product reorder levels
stock_with_threshold = stock_summary.join(products, on="product_id", how="left")

# Step 6: Flag understocked & overstocked
stock_status = stock_with_threshold.withColumn(
    "status",
    when(col("total_stock") < col("reorder_level"), "Understocked")
    .when(col("total_stock") > col("reorder_level") * 5, "Overstocked")  # Example rule
    .otherwise("Normal")
)

# Step 7: Save results to file
stock_status.write.csv("warehouse_stock_status.csv", header=True)

# Show sample
stock_status.show(20, truncate=False)
