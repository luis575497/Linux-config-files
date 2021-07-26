#!/usr/bin/bash
# Programa para crear un entorno de python para proyectos

# Colores
RED="\e[31m"
GREEN="\e[32m"
YELLOW="\e[33m"
ENDCOLOR="\e[0m"

# Variables globales
VER="1.0.0"
nombre=0

# Funciones
function salir() {
    echo -e "${RED}[*]   Saliendo del script ....${ENDCOLOR}"
    exit 1
}

function ayuda() {
    echo -e "${YELLOW}[*]   Estructura del programa:  ${ENDCOLOR}"
    echo -e "${YELLOW}[*]   pyproyect [Nombre de la carpeta] -p [Paquetes para python venv]${ENDCOLOR}"
    #echo ""
    #echo -e "${YELLOW} ${ENDCOLOR}"
    #echo -e "${YELLOW} ${ENDCOLOR}"
}

function tareas() {
    echo -e "${GREEN}[*]    Creando carpeta $1 ${ENDCOLOR}"
    mkdir "$1"

    echo -e "${GREEN}[*]    Entrando en carpeta $1 ${ENDCOLOR}"
    cd $1

    echo -e "${GREEN}[*]    Creando entorno virtual de python ${ENDCOLOR}"
    python -m venv venv

    echo -e "${GREEN}[*]    Activando entorno de python ${ENDCOLOR}"
    source "./venv/bin/activate"
    
    if [[ -n $2 ]]; then
        echo -e "${GREEN}[*]    Instalando paquetes${ENDCOLOR}"
        python -m pip install --upgrade pip
        pip install $paquetes
    fi

    echo -e "${GREEN}[*]    Iniciando repositorio git${ENDCOLOR}"
    git init

    echo -e "${GREEN}[*]    Creando archivo .gitignore ${ENDCOLOR}"
    echo "venv/**/*" > .gitignore
}

# Interrupciones de ejecucion
trap salir INT HUP TERM KILL

# Manejo de opciones y argumentos
while getopts ":p:n: hv" options; do
    case $options in 
        p) echo -e "${GREEN}Paquetes a instalar: $OPTARG ${ENDCOLOR}"
           paquetes=$OPTARG 
            ;;
        n) echo -e "${GREEN}Nombre de la carpeta: $OPTARG ${ENDCOLOR}"
           nombre=$OPTARG 
            ;;
        h) ayuda
            ;;
        v) echo -e "${YELLOW}   Version $VER ${ENDCOLOR}"
           echo "" 
            ;;
        :) echo -e "${RED}La Opcion $OPTARG necesita de un argumento ${ENDCOLOR}"
           salir
            ;;
        \?) echo -e "${YELLOW}  Opcion invalida ${ENDCOLOR}"
            echo -e "${YELLOW}  Para ayuda ponga el siguiente comando: pyproyect -h ${ENDCOLOR}"
            salir
            ;;
    esac
done

# Cuerpo
if [[ $# == 0 ]]; then
    ayuda
    salir
fi

echo ""
tareas $nombre $paquetes

