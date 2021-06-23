# Mi configuración para Linux basado en arch

1. Oh my bash
2. Yaourt
3. Vim
4. Qtile
5. Rofi
6. feh
7. Picom
  - Especificar la ubicación del archivo de configuración
  - Ejecutar esta version de picom para efectos y transiciones `yaourt -S picom-jonaburg-git`
8. Nerd Fonts
9. Alacritty
10. Fzf
11. Bat
  - Agregar a bashrc el alias `alias cat="bat"`
13. Drivers de Amd
14. Tema para Grub
  - Arch Silence se puede instalar des AUR con el siguiente comando `yaourt -S arch-silence-grub-theme-git`
  - Modificar en el archivo de configuración la ubicacion del tema
15. Lightdm
  - Instalar el un greeter `yaourt -S lightdm-webkit-greeter`
  - Instalar el tema `yaourt -S lightdm-webkit-theme-aether`
  - Detener el administrador de pantalla que se esté utilizando `systemctl stop sddm`
  - Hablitar lightdm `systemctl enable lightdm.service`
16. Cambiar el comando ls
  - Instalar Exa `sudo pacman -S exa`
  - Establecer los alias en el bashrc `alias ll="exa --long -all" 
