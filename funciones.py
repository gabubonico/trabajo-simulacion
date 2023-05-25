import random

def fac(n):
    if n == 0:
        return 1
    else:
        return n * fac(n - 1)

def compose(n, x):
    return fac(n)/(fac(x) * fac(n - x))

def probabilidad_binomial(x, n, p):
    return compose(n, x) * pow(p, x) * pow(1-p,x-n)

def distribucion(n, p):
    resul = []

    for i in range(n):
        resul.append(probabilidad_binomial(i, n, p))

    return resul
