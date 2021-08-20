#!/usr/bin/bash
sed -n '/STARTKEYB/,/ENDKEYB/p' ~/.config/qtile/config.py | \
    grep "^    Key" | \
    sed 's/, lazy.*), desc/ /' | \
    tr -d "\"\'\[\]" | \
    sed 's/Key(//;s/),//;s/control/Ctrl/;s/Return/Enter/;s/mod//' | \
    tr "," "+" | \
    sed 's/+/ +/;s/shift+/Shift +/;s/Ctrl+/Ctrl +/;s/space/Space/' | \
    awk -F = 'BEGIN {printf "%-25s %s\n","    Comandos", "Explicación"}
    {printf "%-25s %s\n", $1, $2}' | \
    yad --geometry=950x700 --title="Atajos de teclado Qtile" --text-info 2>/dev/null
