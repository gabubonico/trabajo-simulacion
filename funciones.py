import random

def ber(p):
    if random.random() <= p:
        return 1
    else:
        return 0


