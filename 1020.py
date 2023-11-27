D = int(input())

dias = [365, 30]
resultado = []

for dia in dias:
    qtd_dias = D // dia
    resultado.append(qtd_dias)
    D %= dia
    if D < 30:
        resultado.append(D)

print("{} ano(s)".format(resultado[0]))
print("{} mes(es)".format(resultado[1]))
print("{} dia(s)".format(resultado[2]))
