import random
import sys
import statistics
import math

# variables de bernoulli
def ber(p):
    if random.random() <= p:
        # pasa la prueba
        return True
    else:
        # no pasa la prueba
        return False

# variables binomiales
def bin(p):
    # variable que recoge el numero de exitos
    exitos = 0

    # ejecutamos 100 pruebas de bernoulli
    for _ in range(100):
        if ber(p):
            exitos += 1

    # devolvemos el numero de exitos
    return exitos

# muestra de valores binomiales
def valores_binomial(n, p):
    # almacenaremos los resultados en un array
    resultado = []

    # generamos n valores de la distribucion binomial
    for _ in range(n):
        x = bin(p)

        # y los añadimos al resultado
        resultado.append(x)

    # devolvemos el array de valores
    return resultado

# calcular la media
def media(X):
    suma = sum(X)
    media = suma / len(X)
    return media

# calcular la varianza
def varianza(X):
    var = statistics.variance(X)
    return var

# calcular la muestra Y
def valores_y(X, m, v):
    Y = []

    # iteramos por todos los valores de X
    for x in X:
        y = (x - m)/math.sqrt(v)
        Y.append(y)

    return Y

######### MAIN ##########
def main():
    input("Bienvenido a mi trabajo de simulacion (presione ENTER para continuar)")

    # introducimos n
    n = int(input("Inserte un tamano de muestra n (mayor que 0) para continuar: "))
    while n <= 0:
        n = int(input("Error. Inserte un tamano de muestra n (mayor que 0) para continuar: "))

    # introducimos p
    p = float(input("a continuacion, inserte la probabilidad p: "))
    while p < 0 or p > 1:
        float(input("error. a continuacion, inserte la probabilidad p: "))

    # generamos la muestra de valores
    print("generando muestra...")
    valores = sorted(valores_binomial(n, p))

    print("la muestra ha sido generada")

    # muestra los valores por terminal si recibe el argumento --verbose
    if len(sys.argv) > 1 and sys.argv[1] == "--verbose":
        print("los valores son estos: ")
        print(valores)
    
    # Contar la frecuencia de cada valor
    frequencies = {}
    for value in valores:
        frequencies[value] = frequencies.get(value, 0) + 1

    # Guardar los datos en un archivo
    with open('binomial.txt', 'w') as file:
        for value, frequency in frequencies.items():
            file.write(f"{value} {frequency}\n")

    print("los datos de la distribucion binomial han sido guardados en el fichero binomial.txt")
    input("usa 'gnuplot binomial.p' para generar el historiograma (ENTER para continuar)")

    # estimacion puntual de la media y la varianza
    m = media(valores)
    v = varianza(valores)

    print("la media de esta muestra es: ")
    print(m)
    print("la varianza de esta muestra es: ")
    print(v)
    input("presione ENTER para continuar")

    # generacion de la muestra Y
    print("generamos la muestra Y (teorema central del límite)")
    valores_Y = sorted(valores_y(valores, m, v))
    print("la muestra ha sido generada")

    # muestra los valores por terminal si recibe el argumento --verbose
    if len(sys.argv) > 1 and sys.argv[1] == "--verbose":
        print("los valores son estos: ")
        print(valores_Y)

    # calculamos que la media y la desviacion tipica
    print("La media de la muestra Y es: ")
    print(media(valores_Y))
    print("la desviacion estandar de la muestra Y es: ")
    print(math.sqrt(varianza(valores_Y)))
    print("advertencia: puede ser que los valores no sean exactamente 0 y 1 respectivamente")
    print("esto puede ser debido a los errores de coma flotante")

    # termina el programa
    input("ha concluido el programa (presiona ENTER para terminar)")


if __name__ == "__main__":
    main()
