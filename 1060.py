lista = []
contador = 0

for i in range(0, 6):
    a = float(input())
    if a > 0:
        contador += 1

print("{} valores positivos".format(contador))
