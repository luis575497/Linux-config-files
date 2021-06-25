import os, time
import random

def cambiar_fondo():
    # Indicar la ubicacion de la carpeta con los fondos de escritorios
    img_ub = "/home/luiyvane/Imágenes"
    # Listar las imagenes
    list_imagenes = os.listdir(img_ub)
    # Obtener la ruta completa de cada imagenes
    paht_img = [f"{img_ub}/{i}" for i in list_imagenes]

    # Array para selccionar las posiciones de manera aleatoria y poder eliminar las posiciones que se han seleccionado
    posiciones = [n for n in range(len(paht_img))]

    while True:
        # Si el array esta vacio se vuelve a generar el mismo
        if len(posiciones) == 0:
            posiciones = [n for n in range(len(paht_img))]

        img_selec = random.choice(posiciones)
        print(img_selec)
        os.system(f"feh --bg-fill {paht_img[img_selec]}")
        time.sleep(500)
        posiciones.remove(img_selec) # Eliminar la posicion de la imagen seleccionada

if __name__ == '__main__':
    cambiar_fondo()
