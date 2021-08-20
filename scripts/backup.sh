#!/usr/bin/bash

cp ~/.bashrc ~/Linux-config-files/
cp /etc/vimrc ~/Linux-config-files/
cp -r ~/Imágenes/* ~/Linux-config-files/wallpapers/
cp -r ~/scripts/* ~/Linux-config-files/scripts
cp ~/.config/alacritty/alacritty.yml ~/Linux-config-files/config/alacritty
cp ~/.config/dunst/dunstrc ~/Linux-config-files/config/dunst/
cp ~/.config/picom/picom.conf ~/Linux-config-files/config/picom
cp ~/.config/qtile/* ~/Linux-config-files/config/qtile/
cp ~/.config/starship.toml ~/Linux-config-files/config/

cd ~/Linux-config-files
git add .
git commit -m "Update automatic"
git push origin main

