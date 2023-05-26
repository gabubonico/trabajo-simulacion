set datafile separator " "  # Establecer el separador de columnas
set style data histogram  # Establecer el estilo del gráfico como histograma
set style fill solid  # Rellenar las barras del histograma
set boxwidth 0.8  # Ajustar el ancho de las barras del histograma
set term png  # Establecer el tipo de terminal como PNG
set terminal png size 1200,600  # Establecer el tamaño de la imagen PNG
set output 'histograma.png'  # Especificar el nombre del archivo de salida
plot 'binomial.txt' using 2:xtic(1) with boxes  # Generar el histograma