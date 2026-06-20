import os
import zipfile
import rarfile
import shutil


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


    os.makedirs(
        carpeta_extraidos,
        exist_ok=True
    )



    archivos = os.listdir(
        carpeta_originales
    )


    print("ARCHIVOS ENCONTRADOS:")
    print(archivos)



    for archivo in archivos:


        ruta_archivo = os.path.join(
            carpeta_originales,
            archivo
        )


        # Evitar carpeta extraidos

        if archivo == "extraidos":

            continue



        # -------------------------
        # ZIP
        # -------------------------

        if archivo.lower().endswith(".zip"):


            print("Extrayendo ZIP:")
            print(archivo)


            try:

                with zipfile.ZipFile(
                    ruta_archivo,
                    "r"
                ) as zip_ref:


                    for miembro in zip_ref.namelist():


                        destino = os.path.join(
                            carpeta_extraidos,
                            miembro
                        )


                        # reemplazar si existe

                        if os.path.exists(destino):

                            os.remove(destino)


                    zip_ref.extractall(
                        carpeta_extraidos
                    )


                print("OK:", archivo)


            except Exception as error:


                print("ERROR ZIP:", archivo)

                print(error)




        # -------------------------
        # RAR
        # -------------------------

        elif archivo.lower().endswith(".rar"):


            print("Extrayendo RAR:")
            print(archivo)


            try:


                with rarfile.RarFile(
                    ruta_archivo,
                    "r"
                ) as rar_ref:


                    rar_ref.extractall(
                        carpeta_extraidos
                    )


                print("OK:", archivo)



            except Exception as error:


                print("NO SE PUDO EXTRAER:", archivo)

                print(error)




        # -------------------------
        # CSV
        # -------------------------

        elif archivo.lower().endswith(".csv"):


            print("Copiando CSV:")
            print(archivo)


            destino = os.path.join(
                carpeta_extraidos,
                archivo
            )


            # reemplazar si existe

            shutil.copy2(
                ruta_archivo,
                destino
            )


            print("OK:", archivo)




print("--------------------------------")
print("PROCESO COMPLETO")
print("INGRESOS + EGRESOS LISTOS")