#/usr/bin/bash

#Colores
RED="\e[31m"

# Variables
nivel_max=98
nivel_min=7

# Funciones
function salir {
    echo -e "${RED}[*]  Saliendo del script de noificaciones personalizadas"
    exit 1
}

# Interrupciones de ejecucion
trap salir INT


# Body
battery_level=$(acpi -b | awk -F , '{printf $2}' | tr -d '%')
estado=$(acpi -b | awk -F , '{printf $1}' | awk '{printf $3}')

if [[ $battery_level -gt $nivel_max ]] && [[ $estado == "Charging" ]] ; then 
    notify-send "Cargado a tope" "Se encuentra cargada la laptop, porfavor desconecte de la corriente"
fi
    
if [[ $battery_level -lt $nivel_min ]] && [[ $estado == "Discharging" ]] ; then 
    notify-send "Bateria Baja" "Conecte su laptop a una fuente de energia lo antes posible"
fi


