# Mi configuración para Linux
La creación de un entorno de trabajo en el cual estemos cómodos es esencial para elevar nuestros niveles de productividad. Linux es un sistema operativo que nos brinda la posibilidad de modificarlo a nuestro gusto, razon por la cual decidí empezar a crear un entorno que se adapte a mis necesidades, a continuación se ve un ejemplo de como se ve mi configuración

IMAGEN

0. Firefox
1. Yaourt
2. Vim
   - Instalar desde AUR youcompleteme `yaourt -S vim-youcompleteme-git`
3. Qtile
    1. Rofi (Lanzador de aplicaciones)
        - Instalar desde pacman los `iconos papirus-icon-theme`
    2. feh (Cambiar el fondo de pantalla)
    3. Picom (Compositor de ventanas, transparencia)
       - Especificar la ubicación del archivo de configuración
       - Ejecutar esta version de picom para efectos y transiciones `yaourt -S picom-jonaburg-git`
    4. Firejail (ejecutar de manera segura el navegador)
    5. Fuente Fira Sans Medium 
4. Herramientas para el terminal
    1. Alacritty
    2. Starship prompt
    3. Nerd Fonts
    5. Fzf
    6. Bat
       - Agregar a bashrc el alias `alias cat="bat"`
    7. Exa
       - Instalar Exa `sudo pacman -S exa`
       - Establecer los alias en el bashrc `alias ll="exa --long -all"
    8. Ranger (terminal file manager)
5. Drivers de Amd
   - Instalar `sudo pacman -S mesa`
6. Tema para Grub
   - Arch Silence se puede instalar des AUR con el siguiente comando `yaourt -S arch-silence-grub-theme-git`
   - Modificar en el archivo de configuración la ubicacion del tema
7. Lightdm
   - Instalar el un greeter `yaourt -S lightdm-webkit-greeter`
   - Instalar el tema `yaourt -S lightdm-webkit-theme-aether`
   - Detener el administrador de pantalla que se esté utilizando `systemctl stop sddm`
   - Hablitar lightdm `systemctl enable lightdm.service`
8. Xranrd para controlar los valores de la pantalla
   - `sudo pacman -S xorg-xrandr`
9. Dunst (servidor de notificaciones)
   - Instalar lo siguiente `sudo pacman -S dunst libnotify`
   - Agregar al xinitrc la el programa dunst ejecuntandose en segundo plano
10. Programas útiles
    1. Siv (Visualizador de imagenes
    2. Thunar (file manager)
        - instalar thunar `sudo pacman -S thunar`
        - instalar un administrador de temas gtk `sudo pacman -S lxappearance`
        - instalr el tema Arc para gtk `yaourt -S arc-gtk-theme`
    3. Zathura
        - Instalar Plugins para leer los diferentes formatos 
