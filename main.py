import random
import sys
import statistics

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

if __name__ == "__main__":
    main()
