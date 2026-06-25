import os
import zipfile
import shutil
import subprocess


# -------------------------
# CONFIGURACIÓN
# -------------------------

tipos_datos = [
    "ingresos",
    "egresos"
]


# -------------------------
# PROCESAR INGRESOS Y EGRESOS
# -------------------------

for tipo_dato in tipos_datos:

    print("--------------------------------")
    print("PROCESANDO:", tipo_dato)
    print("--------------------------------")

    carpeta_originales = os.path.join(
        os.path.dirname(__file__),
        "..",
        "datos",
        tipo_dato,
        "archivos_originales"
    )

    carpeta_extraidos = os.path.join(
        carpeta_originales,
        "extraidos"
    )


    # -------------------------
    # LIMPIEZA COMPLETA (IMPORTANTE)
    # -------------------------

    if os.path.exists(carpeta_extraidos):
        shutil.rmtree(carpeta_extraidos)

    os.makedirs(
        carpeta_extraidos,
        exist_ok=True
    )


    # -------------------------
    # LISTAR ARCHIVOS
    # -------------------------

    archivos = os.listdir(carpeta_originales)

    print("ARCHIVOS ENCONTRADOS:")
    print(archivos)


    # -------------------------
    # PROCESAR ARCHIVOS
    # -------------------------

    for archivo in archivos:

        ruta_archivo = os.path.join(
            carpeta_originales,
            archivo
        )

        # evitar carpeta extraidos si aparece
        if archivo == "extraidos":
            continue


        # -------------------------
        # ZIP
        # -------------------------

        if archivo.lower().endswith(".zip"):

            print("Extrayendo ZIP:", archivo)

            try:
                with zipfile.ZipFile(ruta_archivo, "r") as zip_ref:
                    zip_ref.extractall(carpeta_extraidos)

                print("OK:", archivo)

            except Exception as error:
                print("ERROR ZIP:", archivo)
                print(error)


        # -------------------------
        # RAR (UNAR)
        # -------------------------

        elif archivo.lower().endswith(".rar"):

            print("Extrayendo RAR:", archivo)

            try:
                subprocess.run(
                    ["unar", "-o", carpeta_extraidos, ruta_archivo],
                    check=True
                )

                print("OK:", archivo)

            except Exception as error:
                print("ERROR RAR:", archivo)
                print(error)


        # -------------------------
        # CSV
        # -------------------------

        elif archivo.lower().endswith(".csv"):

            print("Copiando CSV:", archivo)

            destino = os.path.join(
                carpeta_extraidos,
                archivo
            )

            shutil.copy2(ruta_archivo, destino)

            print("OK:", archivo)


print("--------------------------------")
print("PROCESO COMPLETO")
print("INGRESOS + EGRESOS LISTOS")