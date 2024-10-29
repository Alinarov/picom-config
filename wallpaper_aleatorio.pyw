#!/usr/bin/env python
import os
import random
import time
import subprocess

# Ruta a la carpeta de imágenes
carpeta_imagenes = '/home/merkaba/Imágenes'

def cambiar_fondo(imagen):
    subprocess.call(['feh', '--bg-scale', imagen])

def obtener_imagenes(carpeta):
    return [os.path.join(carpeta, f) for f in os.listdir(carpeta) if f.endswith(('jpg', 'jpeg', 'png', 'bmp'))]

def main():
    imagenes = obtener_imagenes(carpeta_imagenes)

    while True:
        if imagenes:  # Asegúrate de que la lista de imágenes no esté vacía
            imagen_seleccionada = random.choice(imagenes)
            cambiar_fondo(imagen_seleccionada)
            print(f"Cambiando a la imagen: {imagen_seleccionada}")
        else:
            print("No se encontraron imágenes en la carpeta.")
            break

        time.sleep(500)  # Espera 10 minutos (600 segundos)

if __name__ == '__main__':
    main()
