N = int(input())
coelho, rato, sapo = 0, 0, 0

for i in range(N):
    num, tipo = map(str, input().split())
    num = int(num)
    if tipo == 'C':
        coelho += num
    elif tipo == 'R':
        rato += num
    elif tipo == 'S':
        sapo += num

total = coelho + rato + sapo
per_coelho = (coelho * 100) / total
per_rato = (rato * 100) / total
per_sapo = (sapo * 100) / total
print("Total: {} cobaias\nTotal de coelhos: {}\nTotal de ratos: {}\nTotal de sapos: {}\nPercentual de coelhos: {:.2f} %\nPercentual de ratos: {:.2f} %\nPercentual de sapos: {:.2f} %".format(total, coelho, rato, sapo, per_coelho, per_rato, per_sapo))
