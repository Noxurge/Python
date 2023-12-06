N = int(input())
lista = []

if N < 10000:
    for X in range(N):
        A = int(input())
        lista.append(A)

for NUM in lista:
    if -10 ** 7 < NUM < 10 ** 7:
        if NUM < 0 and NUM % 2 != 0:
            print("ODD NEGATIVE")
        elif NUM < 0 and NUM % 2 == 0:
            print("EVEN NEGATIVE")
        elif NUM == 0:
            print("NULL")
        elif NUM > 0 and NUM % 2 != 0:
            print("ODD POSITIVE")
        elif NUM > 0 and NUM % 2 == 0:
            print("EVEN POSITIVE")
