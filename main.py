import random

def ber(p):
    if random.random() <= p:
        # pasa la prueba
        return true
    else:
        # no pasa la prueba
        return false

def bin(p):
    # variable que recoge el numero de exitos
    exitos = 0

    # ejecutamos 100 pruebas de bernoulli
    for _ in range(100):
        if ber(p):
            ++exitos

    # devolvemos el numero de exitos
    return exitos

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
    valores = valores_binomial(n, p)

    print("la muestra ha sido generada")

if __name__ == "__main__":
    main()
