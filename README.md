# Mi configuración para Linux (Manjaro)
La creación de un entorno de trabajo en el cual estemos cómodos es esencial para elevar nuestros niveles de productividad. Linux es un sistema operativo que nos brinda la posibilidad de modificarlo a nuestro gusto, razon por la cual decidí empezar a crear un entorno que se adapte a mis necesidades, a continuación se ve un ejemplo de como se ve mi configuración

IMAGEN

1. Starship prompt
2. Yaourt
3. Vim
  - Instalar desde AUR youcompleteme `yaourt -S vim-youcompleteme-git`
5. Qtile
  - a;
7. Rofi
8. feh
9. Picom
  - Especificar la ubicación del archivo de configuración
  - Ejecutar esta version de picom para efectos y transiciones `yaourt -S picom-jonaburg-git`
10. Nerd Fonts
11. Alacritty
12. Fzf
13. Bat
  - Agregar a bashrc el alias `alias cat="bat"`
14. Drivers de Amd
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
18. Xranrd para controlar los valores de la pantalla
  - `sudo pacman -S xorg-xrandr`
20. Dunst
  - Instalar lo siguiente `sudo pacman -S dunst libnotify`
  - Agregar al xinitrc la el programa dunst ejecuntandose en segundo plano
22. Siv (Visualizador de imagenes
24. Thunar (file manager)
  - instalar thunar `sudo pacman -S thunar`
  - instalar un administrador de temas gtk `sudo pacman -S lxappearance`
  - instalr el tema Arc para gtk `yaourt -S arc-gtk-theme`
