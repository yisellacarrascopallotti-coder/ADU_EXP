import requests
from bs4 import BeautifulSoup
import os


# Página de Aduanas
pagina = "https://www.aduana.cl/copia-de-base-de-datos-operaciones-de-ingreso/aduana/2024-11-12/122745.html"


# Carpeta donde guardaremos archivos
carpeta = os.path.join(
    os.path.dirname(__file__),
    "..",
    "datos",
    "ingresos",
    "archivos_originales"
)

# Crear carpeta si no existe
os.makedirs(carpeta, exist_ok=True)


# Leer página
respuesta = requests.get(pagina)

soup = BeautifulSoup(
    respuesta.text,
    "html.parser"
)


# Buscar enlaces
enlaces = soup.find_all("a")


for enlace in enlaces:

    año = enlace.text.strip()
    archivo = enlace.get("href")


    if archivo and año.isdigit():

        url_archivo = "https://www.aduana.cl" + archivo


        print(f"Descargando {año}...")


        contenido = requests.get(url_archivo)


        nombre = url_archivo.split("/")[-1]


        ruta = os.path.join(
            carpeta,
            nombre
        )


        with open(ruta, "wb") as f:
            f.write(contenido.content)


        print("Guardado:", nombre)