#!/bin/bash
if [ -z "$1" ]; then
	echo "Error: Debes proporcionar el nombre del directorio."
	exit 1
fi

directorio="$1"

archivo_salida="atributos_archivos.txt"

if [ ! -d "$directorio" ]; then
	echo "Error: El directorio $directorio no existe."
	exit 1
fi

> "$archivo_salida"

for archivo in "$directorio"/*; do
	if [ -f "$archivo" ]; then
	
	permisos=$(stat -c "%A" "$archivo")
	usuario=$(stat -c "%U" "$archivo")
	grupo=$(stat -c "%G" "$archivo")
	bytes=$(stat -c "%s" "$archivo")
	fecha_modificacion=$(stat -c "%y" "$archivo")
	nombre_archivo=$(basename "$archivo")
	
	echo "Archivo: $nombre_archivo" >> "$archivo_salida"
	echo "Permisos: $permisos" >> "$archivo_salida"
	echo "Usuario: $usuario" >> "$archivo_salida"
	echo "Grupo: $grupo" >> "$archivo_salida"
	echo "Bytes: $bytes" >> "$archivo_salida"
	echo "Ultima modificación: $fecha_modificacion" >> "$archivo_salida"
	echo "----------------------------------------" >> "$archivo_salida"
     fi
done
echo "Ejecutado por: Adrian Alejandro Gaspar Corona"
echo "Matrícula: 03093676"
echo "Fecha de ejecución:" $(date)

