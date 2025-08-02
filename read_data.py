from pyspark.sql import SparkSession
spark= SparkSession.builder.appName("SimpleApp").getOrCreate()
spark.range(5).show()
spark.stop()
