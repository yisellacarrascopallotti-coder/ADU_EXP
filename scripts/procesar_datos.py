import pandas as pd
import os


def leer_csv(ruta_archivo):

    df = pd.read_csv(
        ruta_archivo,
        sep=";",
        encoding="latin1"
    )

    return df



# -------------------------
# INGRESOS
# -------------------------

archivo_ingresos = os.path.join(
    os.path.dirname(__file__),
    "..",
    "datos",
    "ingresos",
    "archivos_originales",
    "ingresos_2024.csv"
)


df_ingresos = leer_csv(archivo_ingresos)


print("TABLA INGRESOS")
print(df_ingresos.head())

print(df_ingresos.shape)



# -------------------------
# EGRESOS
# -------------------------

carpeta_egresos = os.path.join(
    os.path.dirname(__file__),
    "..",
    "datos",
    "egresos",
    "archivos_originales"
)


print("ARCHIVOS EGRESOS")

print(os.listdir(carpeta_egresos))

# -------------------------
# LEER EGRESOS 2024
# -------------------------

archivo_egresos = os.path.join(
    os.path.dirname(__file__),
    "..",
    "datos",
    "egresos",
    "archivos_originales",
    "salidas_2024.csv"
)


df_egresos = leer_csv(archivo_egresos)


print("TABLA EGRESOS")

print(df_egresos.head())

print(df_egresos.shape)

print("COLUMNAS INGRESOS")
print(df_ingresos.columns)


print("COLUMNAS EGRESOS")
print(df_egresos.columns)

# -------------------------
# LIMPIEZA DE TIPOS
# -------------------------

df_ingresos["PERIODO"] = (
    df_ingresos["PERIODO"]
    .str.replace(",00", "")
    .astype(int)
)

df_egresos["PERIODO"] = (
    df_egresos["PERIODO"]
    .astype(int)
)

df_ingresos["MES"] = (
    df_ingresos["MES"]
    .str.replace(",00", "")
    .astype(int)
)

df_egresos["MES"] = (
    df_egresos["MES"]
    .astype(int)
)

print(df_ingresos[["PERIODO","MES"]].head())

print(df_egresos[["PERIODO","MES"]].head())