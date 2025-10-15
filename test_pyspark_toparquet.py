from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.types import (StructType, StructField, StringType, IntegerType, FloatType, DoubleType, TimestampType)
import json
import os

os.environ["JAVA_HOME"] = r"C:\Program Files\Eclipse Adoptium\jdk-17.0.16.8-hotspot"
os.environ["HADOOP_HOME"] = r"C:\hadoop-3.3.1"
os.environ["PATH"] += ";" + os.path.join(os.environ["HADOOP_HOME"], "bin")

spark = SparkSession.builder \
    .appName("LocalTest") \
    .config("spark.driver.memory", "4g") \
    .getOrCreate()

input_dir = "./parsed_output/"
output_dir = "./test_output/"

df = spark.read.option("header", True).csv(input_dir)
print(df.head())