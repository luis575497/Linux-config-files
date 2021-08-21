#!/usr/bin/bash

cp /home/luiyvane/.bashrc ~/Linux-config-files/
cp /etc/vimrc /home/luiyvane/Linux-config-files/
cp -r /home/luiyvane/Imágenes/* /home/luiyvane/Linux-config-files/wallpapers/
cp -r /home/luiyvane/scripts/* /home/luiyvane/Linux-config-files/scripts
cp /home/luiyvane/.config/alacritty/alacritty.yml /home/luiyvane/Linux-config-files/config/alacritty
cp /home/luiyvane/.config/dunst/dunstrc /home/luiyvane/Linux-config-files/config/dunst/
cp /home/luiyvane/.config/picom/picom.conf /home/luiyvane/Linux-config-files/config/picom
cp -r /home/luiyvane/.config/qtile/* /home/luiyvane/Linux-config-files/config/qtile/
cp /home/luiyvane/.config/starship.toml ~/Linux-config-files/config/

cd /home/luiyvane/Linux-config-files
git add .
git commit -m "Update automatic"
git push origin main

