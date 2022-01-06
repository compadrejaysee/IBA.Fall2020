import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, DoubleType
from pyspark.sql.functions import col
from pyspark.sql.functions import udf

# UDF for rounding values
def round_off(n):
	return round(n,4)

# UDF for (open x close) / close
def calculations(_open, close):
	return (_open + close) / close

# Creating spark session
spark = SparkSession.builder.appName('Ibrahim').getOrCreate()

# Creating schema for the data set
schema = StructType() \
      .add("time",StringType(),True) \
      .add("open",DoubleType(),True) \
      .add("close",DoubleType(),True) \
      .add("high",DoubleType(),True) \
      .add("low",DoubleType(),True) \
      .add("volume",DoubleType(),True)

# Registering UDFs
round_off_udf = udf(round_off, DoubleType())
calculations_udf = udf(calculations, DoubleType())

# Reading data from the csv
df = spark.read.format("csv").option("header", True).schema(schema).load("zilusd.csv")

# Rounding off values of the columns
df = df.withColumn("open",round_off_udf(col("open")))
df = df.withColumn("close",round_off_udf(col("close")))
df = df.withColumn("high",round_off_udf(col("high")))
df = df.withColumn("low",round_off_udf(col("low")))
df = df.withColumn("volume",round_off_udf(col("volume")))
df.show()

# Calculating the min max and average of the volume
maximum = df.agg({"volume": "max"}).collect()[0]["max(volume)"]
minimum = df.agg({"volume": "min"}).collect()[0]["min(volume)"]
average = df.agg({"volume": "avg"}).collect()[0]["avg(volume)"]
print("Average of volume is:", maximum)
print("Minimum of volume is:", minimum)
print("Maximum of volume is:", average)

# Dropping duplicate rows (if any) from the data set
df = df.dropDuplicates()
df.show()

# Creating new column for (open x close) / close
df = df.withColumn("Calculations",calculations_udf('open', 'close'))
df.show()

# Sorting the data based on Volume
df = df.orderBy('volume')
df.show()

df_lt_average = df.filter(df.volume < average)
df_gte_average = df.filter(df.volume >= average)
df_lt_average.write.csv('volume_lt_avg')
df_gte_average.write.csv('volume_gte_avg')


# df.printSchema()