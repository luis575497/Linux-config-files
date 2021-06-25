import os, time

img_ub = "/home/luiyvane/Imágenes"
list_imagenes = os.listdir(img_ub)

paht_img = [f"{img_ub}/{i}" for i in list_imagenes]

pos=0

while True:
    os.system(f"feh --bg-fill {paht_img[pos % len(paht_img)]}")
    time.sleep(630)
    pos+=1
