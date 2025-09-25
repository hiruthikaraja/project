# Week 3: Store-Level Insights (PySpark)

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg, month, year

spark = SparkSession.builder.appName("StoreLevelInsights").getOrCreate()

# Sample sales data (20 rows)
data = [
    (1,1,1,'2025-01-05',2,110000),(2,1,2,'2025-01-10',5,12500),
    (3,2,3,'2025-01-12',3,4500),(4,2,4,'2025-01-15',2,6000),
    (5,3,5,'2025-02-03',1,35000),(6,3,6,'2025-02-10',2,90000),
    (7,4,7,'2025-02-12',3,12000),(8,4,8,'2025-02-15',1,12000),
    (9,5,9,'2025-03-05',1,65000),(10,5,10,'2025-03-10',4,6000),
    (11,6,11,'2025-03-12',2,90000),(12,6,12,'2025-03-15',1,48000),
    (13,7,13,'2025-04-05',3,12000),(14,7,14,'2025-04-10',2,4000),
    (15,8,15,'2025-04-12',1,12000),(16,8,16,'2025-04-15',2,4000),
    (17,9,17,'2025-05-05',1,65000),(18,9,18,'2025-05-10',1,55000),
    (19,10,19,'2025-05-12',2,3000),(20,10,20,'2025-05-15',1,1500)
]
columns = ["product_id","store_id","employee_id","sale_date","quantity","total_amount"]

df = spark.createDataFrame(data, columns)
df = df.withColumn("sale_date", col("sale_date").cast("date"))

# Filter underperforming products
underperforming = df.filter(col("total_amount") < 10000)

# Average monthly revenue per store
avg_monthly_revenue = underperforming.withColumn("month", month(col("sale_date"))) \
    .withColumn("year", year(col("sale_date"))) \
    .groupBy("store_id","year","month") \
    .agg(avg("total_amount").alias("avg_monthly_revenue")) \
    .orderBy("store_id","year","month")

avg_monthly_revenue.show(truncate=False)
avg_monthly_revenue.coalesce(1).write.csv("underperforming_store_summary.csv", header=True, mode="overwrite")

spark.stop()
