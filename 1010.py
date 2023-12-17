A, B, C = map(lambda x: int(x) if x.isdigit() else float(x), input().split())
A1, B1, C1 = map(lambda x: int(x) if x.isdigit() else float(x), input().split())
total = B * C + B1 * C1
print("VALOR A PAGAR: R$ {:.2f}".format(total))
