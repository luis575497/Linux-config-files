#!/bin/bash
#Autor: Luis Enrique Lescano

# Fondo de Pantalla
python ~/.config/qtile/scriptsq/background_change.py &

# Compositor de ventanas
picom &

# Monitor del sistema
#(conky -c $HOME/.config/qtile/conf_programs/lean-conky-config/conky.conf &)
(conky -c ~/.config/qtile/conf_programs/.conkyrc &)

# Iniciar con el teclado numerico
numlockx on &

# Iniciar servidor de notificaciones
dunst &
