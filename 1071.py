x = int(input())
y = int(input())
lista = []

if x > y:
    x -= 1
    while x > y:
        if x % 2 != 0:
            lista.append(x)
        x -= 1

if y > x:
    y -= 1
    while y > x:
        if y % 2 != 0:
            lista.append(x)
        y -= 1

soma = sum(lista)
print(soma)
