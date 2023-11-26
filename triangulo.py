A, B, C = map(float, input().split())
perimetro = A + B + C
if A + B > C and A + C > B and B + C > A:
    print("Perimetro = {}".format(perimetro))
else:
    area = ((A + B) * C) / 2
    print("Area = {}".format(area))
