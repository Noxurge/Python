inteiro = int(input())
contador = 0

while True:
    if inteiro % 2 != 0:
        print(inteiro)
        inteiro += 2
        contador += 1
        if contador == 6:
            break
    else:
        inteiro += 1
