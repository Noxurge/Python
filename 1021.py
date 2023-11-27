N = int(float(input()) * 100)

if 0 <= N <= 100000000:
    notas = [10000, 5000, 2000, 1000, 500, 200]
    result = []
    moedas = [100, 50, 25, 10, 5, 1]
    result1 = []

    for nota in notas:
        qtd_notas = N // nota
        result.append(qtd_notas)
        N %= nota

    print("NOTAS:")
    for i, nota in enumerate(notas):
        print("{} nota(s) de R$ {:.2f}".format(round(result[i]), nota / 100))
    
    for moeda in moedas:
        qtd_moedas = N // moeda
        result1.append(qtd_moedas)
        N %= moeda
    
    print("MOEDAS:")
    for i, moeda in enumerate(moedas):
        print("{} moeda(s) de R$ {:.2f}".format(round(result1[i]), moeda / 100))
else:
    pass
