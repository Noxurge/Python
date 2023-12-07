N = int(input())
lista = []
if N < 10000:
    for i in range(9999):
        if i % N == 2:
            lista.append(i)

for item in lista:
    print(item)
