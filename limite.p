set style data histogram
set style histogram clustered
set boxwidth 0.9
set xtic rotate by -45
set xtics 1
set yrange [0:*]

# Contar el número de filas en el archivo de datos
stats 'limite.txt' using 0 nooutput
num_filas = STATS_records

# Calcular el índice de la etiqueta central
indice_central = int(num_filas / 2) + 1

set term png  # Establecer el tipo de terminal como PNG
set terminal png size 1200,600  # Establecer el tamaño de la imagen PNG
set output 'limite.png'  # Especificar el nombre del archivo de salida
plot 'limite.txt' using 2:xticlabels(int($0) == indice_central ? stringcolumn(1) : '') with histogram