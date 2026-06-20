import pandas as pd
import os
import glob


def leer_csv(ruta_archivo):

    df = pd.read_csv(
        ruta_archivo,
        sep=";",
        encoding="latin1"
    )

    return df

def limpiar_numero(columna):

    columna = (
        columna
        .astype(str)
        .str.replace(",", ".", regex=False)
    )

    columna = pd.to_numeric(
        columna,
        errors="coerce"
    )

    return columna



# -------------------------
# INGRESOS
# -------------------------

# -------------------------
# CARGAR INGRESOS
# -------------------------

carpeta_ingresos = os.path.join(
    os.path.dirname(__file__),
    "..",
    "datos",
    "ingresos",
    "archivos_originales"
)


# -------------------------
# BUSCAR ARCHIVOS INGRESOS
# -------------------------

archivos_ingresos = glob.glob(
    os.path.join(carpeta_ingresos, "*.csv")
)


archivos_ingresos += glob.glob(
    os.path.join(carpeta_ingresos, "extraidos", "*.csv")
)


print("ARCHIVOS INGRESOS ENCONTRADOS")

print(archivos_ingresos)


# Leer todos los archivos encontrados

lista_ingresos = []

for archivo in archivos_ingresos:

    df = leer_csv(archivo)

    lista_ingresos.append(df)


# Unir todos los años

df_ingresos = pd.concat(
    lista_ingresos,
    ignore_index=True
)


print("TABLA INGRESOS TOTAL")

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
# LEER EGRESOS
# -------------------------

# -------------------------
# BUSCAR ARCHIVOS EGRESOS
# -------------------------

archivos_egresos = glob.glob(
    os.path.join(carpeta_egresos, "*.csv")
)


archivos_egresos += glob.glob(
    os.path.join(carpeta_egresos, "extraidos", "*.csv")
)


print("ARCHIVOS EGRESOS ENCONTRADOS")

print(archivos_egresos)


print("ARCHIVOS EGRESOS ENCONTRADOS")
print(archivos_egresos)


lista_egresos = []


for archivo in archivos_egresos:

    df = leer_csv(archivo)

    lista_egresos.append(df)



df_egresos = pd.concat(
    lista_egresos,
    ignore_index=True
)


print("TABLA EGRESOS TOTAL")

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
    pd.to_numeric(
        df_ingresos["PERIODO"]
        .astype(str)
        .str.replace(",00", ""),
        errors="coerce"
    )
)

df_egresos["PERIODO"] = (
    df_egresos["PERIODO"]
    .astype(int)
)

df_ingresos["MES"] = (
    pd.to_numeric(
        df_ingresos["MES"]
        .astype(str)
        .str.replace(",00", ""),
        errors="coerce"
    )
)

df_egresos["MES"] = (
    df_egresos["MES"]
    .astype(int)
)

print(df_ingresos[["PERIODO","MES"]].head())

print(df_egresos[["PERIODO","MES"]].head())

# -------------------------
# LIMPIEZA MONTOS INGRESOS
# -------------------------

df_ingresos["CIF_US"] = limpiar_numero(
    df_ingresos["CIF_US"]
)


df_ingresos["AD_VALOREM_US"] = limpiar_numero(
    df_ingresos["AD_VALOREM_US"]
)


df_ingresos["CANTIDAD_MERCANCÍA"] = limpiar_numero(
    df_ingresos["CANTIDAD_MERCANCÍA"]
)

# -------------------------
# LIMPIEZA MONTOS EGRESOS
# -------------------------

df_egresos["FOB_US_DUSLEG"] = limpiar_numero(
    df_egresos["FOB_US_DUSLEG"]
)


df_egresos["FOBUS_AJUSTADO_IVV"] = limpiar_numero(
    df_egresos["FOBUS_AJUSTADO_IVV"]
)


df_egresos["CANTIDAD_MERCANCIA"] = limpiar_numero(
    df_egresos["CANTIDAD_MERCANCIA"]
)

print(df_ingresos[[
    "CIF_US",
    "AD_VALOREM_US",
    "CANTIDAD_MERCANCÍA"
]].dtypes)


print(df_egresos[[
    "FOB_US_DUSLEG",
    "FOBUS_AJUSTADO_IVV",
    "CANTIDAD_MERCANCIA"
]].dtypes)