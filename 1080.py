lista = []

for i in range(1, 101):
    N = int(input())
    lista.append(N)

maior = max(lista)
posicao = lista.index(maior) + 1

print("{}\n{}".format(maior, posicao))
