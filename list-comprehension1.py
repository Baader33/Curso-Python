import random

def maxi (valor):
    valor = random.randint(3,33) + 3
    return valor

my_range = range(4)

my_list = [maxi(33) for kk in my_range]

print(my_list)
