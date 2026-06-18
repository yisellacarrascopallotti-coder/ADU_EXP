import requests
from bs4 import BeautifulSoup
import os


# Página de Aduanas - Operaciones de salida (egresos)
pagina = "https://www.aduana.cl/base-de-datos-operaciones-de-salida/aduana/2024-11-12/153724.html"


# Carpeta donde se guardarán los archivos
carpeta = os.path.join(
    os.path.dirname(__file__),
    "..",
    "datos",
    "egresos",
    "archivos_originales"
)

# Crear carpeta si no existe
os.makedirs(carpeta, exist_ok=True)


# Leer página web
respuesta = requests.get(pagina)


soup = BeautifulSoup(
    respuesta.text,
    "html.parser"
)


# Buscar todos los links
enlaces = soup.find_all("a")


for enlace in enlaces:

    año = enlace.text.strip()
    archivo = enlace.get("href")


    # Solo toma los links que tienen años
    if archivo and año.isdigit():

        url_archivo = "https://www.aduana.cl" + archivo


        print(f"Descargando egresos {año}...")


        archivo_descargado = requests.get(url_archivo)


        nombre = url_archivo.split("/")[-1]


        ruta = os.path.join(
            carpeta,
            nombre
        )


        with open(ruta, "wb") as f:
            f.write(archivo_descargado.content)


        print("Guardado:", nombre)