A, B, C = map(float, input().split())
lista = [A, B, C]
lista.sort(reverse=True)
A, B, C = lista[0], lista[1], lista[2]
a_q = A ** 2
b_c = B ** 2 + C ** 2

if A >= B + C:
    print("NAO FORMA TRIANGULO")
elif a_q == b_c:
    print("TRIANGULO RETANGULO")
elif a_q > b_c:
    print("TRIANGULO OBTUSANGULO")
elif a_q < b_c:
    print("TRIANGULO ACUTANGULO")
else:
    pass

if A == B == C:
    print("TRIANGULO EQUILATERO")
elif A == B or A == C or B == C:
    print("TRIANGULO ISOSCELES")
