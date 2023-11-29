valor = float(input())

def impostos(salario):
    if 0 < salario <= 2000:
        print("Isento")
    elif 2000.01 < salario <= 3000:
        imposto = (salario - 2000) * 0.08
        print("R$ {:.2f}".format(imposto))
    elif 3000.01 < salario <= 4500:
        imposto = (1000 * 0.08) + (salario - 3000) * 0.18
        print("R$ {:.2f}".format(imposto))
    else:
        imposto = (1000 * 0.08) + (1500 * 0.18) + (salario - 4500) * 0.28
        print("R$ {:.2f}".format(imposto))

impostos(valor)
