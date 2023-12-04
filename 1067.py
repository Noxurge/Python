inteiro = int(input())
lista = []

if 1 <= inteiro <= 1000:
    for i in range(inteiro):
        if inteiro % 2 != 0:
            lista.append(inteiro)
        inteiro -= 1

lista.reverse()
for i in lista:
    print(i)
