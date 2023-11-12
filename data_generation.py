from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, DoubleType
from datetime import datetime, timedelta
from random import random

# Inicio de sesion Spark
spark = SparkSession.builder.appName("generar-parquet").getOrCreate()

# Crear rango de fechas para los últimos dos años
fecha_inicial = datetime.now() - timedelta(days=365 * 2)
fechas = [fecha_inicial + timedelta(days=d) for d in range(365 * 2)]

# Datos ficticios
data = {
    "fecha": [fecha.strftime("%Y-%m-%d") for fecha in fechas],
    "temperatura": [round((0.0 + (5.0 - 0.0) * random()), 2) + 20 for _ in range(len(fechas))],  # Valores aleatorios entre 20 y 25
    "humedad": [round((0.0 + (20.0 - 0.0) * random()), 2) + 50 for _ in range(len(fechas))],  # Valores aleatorios entre 50 y 70
    "viento": [round((0.0 + (15.0 - 0.0) * random()), 2) + 5 for _ in range(len(fechas))],  # Valores aleatorios entre 5 y 20
    "descripcion": ["Soleado", "Parcialmente nublado", "Mayormente soleado", "Parcialmente nublado", "Soleado"] * (len(fechas) // 5)
}

# Definir el esquema para el DataFrame
schema = StructType([
    StructField("fecha", StringType(), True),
    StructField("temperatura", DoubleType(), True),
    StructField("humedad", DoubleType(), True),
    StructField("viento", DoubleType(), True),
    StructField("descripcion", StringType(), True)
])

# Crear un DataFrame de PySpark con el esquema especificado
df_spark = spark.createDataFrame([(data["fecha"][i], data["temperatura"][i], data["humedad"][i], data["viento"][i], data["descripcion"][i]) for i in range(len(fechas))], schema)

# Guardar los datos en formato Parquet
df_spark.write.parquet("clima_data_2_years.parquet", mode="overwrite")

# Fin de sesión de Spark
spark.stop()
