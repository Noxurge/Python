N = int(input("Digite a quantia que quer trocar: "))
print(f"\nVocê digitou: {N}\n")

if 0 < N < 1000000:
    notas = [100, 50, 20, 10, 5, 2, 1]
    resultado = []

    for nota in notas:
        qtd_notas = N // nota
        resultado.append(qtd_notas)
        N %= nota

    for i, nota in enumerate(notas):
        print("{} nota(s) de R$ {},00".format(resultado[i], nota))
else:
    pass
