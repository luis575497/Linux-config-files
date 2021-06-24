# Mi configuración para Linux basado en arch

1. Starship prompt
2. Yaourt
3. Vim
  - Instalar desde AUR youcompleteme `yaourt -S vim-youcompleteme-git`
5. Qtile
6. Rofi
7. feh
8. Picom
  - Especificar la ubicación del archivo de configuración
  - Ejecutar esta version de picom para efectos y transiciones `yaourt -S picom-jonaburg-git`
9. Nerd Fonts
10. Alacritty
11. Fzf
12. Bat
  - Agregar a bashrc el alias `alias cat="bat"`
13. Drivers de Amd
  - Instalar `sudo pacman -S mesa`
15. Tema para Grub
  - Arch Silence se puede instalar des AUR con el siguiente comando `yaourt -S arch-silence-grub-theme-git`
  - Modificar en el archivo de configuración la ubicacion del tema
16. Lightdm
  - Instalar el un greeter `yaourt -S lightdm-webkit-greeter`
  - Instalar el tema `yaourt -S lightdm-webkit-theme-aether`
  - Detener el administrador de pantalla que se esté utilizando `systemctl stop sddm`
  - Hablitar lightdm `systemctl enable lightdm.service`
17. Cambiar el comando ls
  - Instalar Exa `sudo pacman -S exa`
  - Establecer los alias en el bashrc `alias ll="exa --long -all" 
