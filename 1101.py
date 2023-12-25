lista = []
soma = 0

while True:
    linha = [int (num) for num in input().split(" ")]
    M = min(linha)
    N = max(linha)
    if M <= 0 or N <= 0:
        break
    for i in range(M, N + 1):
        lista.append(i)
    for item in lista:
        soma += item
    print(' '.join(map(str, lista)) + " Sum={}".format(soma))
    lista = []
    soma = 0
