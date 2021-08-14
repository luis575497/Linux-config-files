#!/usr/bin/bash
#Colores
printf "%-25s %s\n" "    Comandos" "Explicación"
sed -n '/STARTKEYB/,/ENDKEYB/p' ~/.config/qtile/config.py | \
    grep "^    Key" | \
    sed 's/, lazy.*), desc/ /' | \
    tr -d "\"\'\[\]" | \
    sed 's/Key(//;s/),//;s/control/Ctrl/;s/Return/Enter/;s/mod//' | \
    tr "," "+" | \
    sed 's/+/ +/;s/shift+/Shift +/;s/Ctrl+/Ctrl +/;s/space/Space/' | \
    awk -F = '{printf "%-25s %s\n", $1, $2}'
