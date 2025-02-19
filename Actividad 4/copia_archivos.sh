#!/bin/bash
if [ -z "$1" ]; then
	echo "Error: Deber proporcionar un nombre de archivo."
	exit 1
fi
archivo_origen="eventos.txt"

archivo_destino="$1"

if [ ! -f "$archivo_origen" ]; then
	echo "Error: El archivo $archivo_origen no existe."
	exit 1
fi

cp "$archivo_origen" "$archivo_destino"

echo "Ejecutado por: Adrian Alejandro Gaspar Corona"
echo "Matrícula: 03093676"
echo "Fecha de ejecución:" $(date)
