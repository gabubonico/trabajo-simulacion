import funciones

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

    # generamos la muestra de probabilidades
    print("generando muestra...")
    dist = funciones.distribucion(n, p)

if __name__ == "__main__":
    main()
