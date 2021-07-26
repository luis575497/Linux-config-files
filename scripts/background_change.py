import os, time
import random

def cambiar_fondo():
    # Indicar la ubicacion de la carpeta con los fondos de escritorios
    img_ub = "/home/luiyvane/Imágenes"
    # Listar las imagenes
    list_imagenes = os.listdir(img_ub)
    # Obtener la ruta completa de cada imagenes
    paht_img = [f"{img_ub}/{i}" for i in list_imagenes]

    while True:
        img_selec = random.choice(paht_img)
        print(img_selec)
        os.system(f"feh --bg-fill {img_selec}")
        time.sleep(500)

if __name__ == '__main__':
    cambiar_fondo()
