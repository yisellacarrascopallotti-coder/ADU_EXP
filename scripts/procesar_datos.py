import pandas as pd
import os


archivo = os.path.join(
    os.path.dirname(__file__),
    "..",
    "datos",
    "ingresos",
    "archivos_originales",
    "ingresos_2024.csv"
)


df = pd.read_csv(
    archivo,
    sep=";",
    encoding="latin1"
)


print(df.head())

print(df.shape)

print(df.columns)

print(df.info())