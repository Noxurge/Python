A, B, C = map(int, input().split())
lista = [A, B, C]
crescente = sorted(lista)

for item in crescente:
    print(item)

print()

for item in lista:
    print(item)
