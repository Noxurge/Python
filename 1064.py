lista = []
contador = 0
numeros = []

for i in range(0, 6):
    a = float(input())
    if a > 0:
        contador += 1
        numeros.append(a)

somar = sum(numeros)
media = somar / contador
print("{} valores positivos".format(contador))
if type(media) == int:
    print(media)
else:
    print("{:.1f}".format(media))
