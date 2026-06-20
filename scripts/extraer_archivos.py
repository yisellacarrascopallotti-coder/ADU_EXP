import os
import zipfile


# -------------------------
# CONFIGURACIÓN
# -------------------------

tipo_dato = "egresos"
# Cambiar a "ingresos" si quieres extraer ingresos


archivo_a_extraer = "salidas_dic_2023.zip"
# Para ingresos sería:
# archivo_a_extraer = "ingresos_dic_2023.zip"



# -------------------------
# RUTAS
# -------------------------

carpeta = os.path.join(
    os.path.dirname(__file__),
    "..",
    "datos",
    tipo_dato,
    "archivos_originales"
)


archivo_zip = os.path.join(
    carpeta,
    archivo_a_extraer
)


destino = os.path.join(
    carpeta,
    "extraidos"
)



# -------------------------
# CREAR CARPETA DESTINO
# -------------------------

os.makedirs(
    destino,
    exist_ok=True
)



# -------------------------
# EXTRAER ZIP
# -------------------------

with zipfile.ZipFile(archivo_zip, "r") as zip_ref:

    zip_ref.extractall(destino)



print("ARCHIVO EXTRAIDO")
print(destino)