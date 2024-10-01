# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 00:55:08 2024

@author: Vaibhav Vilas Pawar
"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *

inputDirectory = "C:/input/"

# Create the SparkSession
spark = SparkSession.\
builder.\
appName("sparkstream").\
getOrCreate()

fileSchema = (StructType([\
                       StructField("userID", IntegerType(), True),
                       StructField("name", StringType(), True),
                       StructField("age",IntegerType(), True),
                       StructField("friends",IntegerType(), True),
                        ]))


inputDF = (spark
.readStream
.format("csv")
.schema(fileSchema)
.load(inputDirectory))

outputDir = "C:/output/"
checkpointDir = "C:/checkpoint/"
resultDF = inputDF

streamingQuery = (resultDF.writeStream
.format("csv")
.option("path", outputDir)
.option("checkpointLocation", checkpointDir)
.start())
