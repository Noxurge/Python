contador = 0

for i in range(5):
    numero = int(input())
    if numero % 2 == 0:
        contador += 1

print('{} valores pares'.format(contador))
