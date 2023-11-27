salario = float(input())

def porcentagem(x):
    porcentagem = (salario * x) / 100
    novo_salario = porcentagem + salario
    print("Novo salario: {:.2f}".format(novo_salario))
    print("Reajuste ganho: {:.2f}".format(porcentagem))
    print("Em percentual: {}%".format(x))

def valor():
    if 0 <= salario <= 400:
        porcentagem(15)
    elif 400.01 <= salario <= 800:
        porcentagem(12)
    elif 800.01 <= salario <= 1200:
        porcentagem(10)
    elif 1200.01 <= salario <= 2000:
        porcentagem(7)
    elif salario > 2000:
        porcentagem(4)

valor()
