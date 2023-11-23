import os
import patoolib


def convert_and_extract_cbr(cbr_file):
    try:
        # Cambiar la extensión de .cbr a .rar
        rar_file = os.path.splitext(cbr_file)[0] + '.rar'
        os.rename(cbr_file, rar_file)
        print(f"Archivo renombrado a {rar_file}")

        # Descomprimir el archivo
        patoolib.extract_archive(rar_file)
        print(f"Archivo descomprimido correctamente.")
    except Exception as e:
        print(f"Error durante el proceso: {e}")


# Ejemplo de uso
# Cambia esto por el nombre de tu archivo CBR
cbr_file_name = input('Nombre del archivo.cbr: ')
cbr_file_name_fin = f"{cbr_file_name}.cbr"
convert_and_extract_cbr(cbr_file_name_fin)
