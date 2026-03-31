from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("AWSDataPipeline").getOrCreate()

# Read data from S3
df = spark.read.json("s3://input-data")

# Basic transformation
df_clean = df.filter(df["value"].isNotNull())

# Write to S3
df_clean.write.mode("overwrite").parquet("s3://output-data")

spark.stop()
