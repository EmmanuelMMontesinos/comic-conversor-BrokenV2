import os


def main():
    # Preguntar por el nombre de la carpeta descomprimida
    comic_name = input("Ingrese el nombre del comic (Carpeta): ")
    # Comprobar si el archivo existe en la carpeta actual
    rename_files(comic_name)


def rename_files(folder_name):
    # Cambia el nombre por los numeros del 1 al total
    carpeta = f"./{folder_name}"
    files = os.listdir(carpeta)
    files.sort()

    # Enumera las paginas
    for i, file_name in enumerate(files):
        # Obtener la extensión del archivo
        _, file_ext = os.path.splitext(file_name)

        # Construir el nuevo nombre de archivo
        new_name = f"{i + 1}{file_ext}"

        # Renombrar el archivo
        os.rename(os.path.join(carpeta, file_name),
                  os.path.join(carpeta, new_name))

    print(f"Archivos dentro de {carpeta} renombrados numéricamente")


if __name__ == "__main__":
    main()
