A, B = map(int, input().split())

def tempo(inicio, fim):
    duracao = (fim - inicio) % 24
    if 1 <= duracao <= 24:
        print("O JOGO DUROU {} HORA(S)".format(duracao))

if A == 0 and B != 0:
    A = 24
    tempo(A, B)
elif B == 0 and A != 0:
    B = 24
    tempo(A, B)
elif A == 0 and B == 0 or B - A == 0:
    print("O JOGO DUROU 24 HORA(S)")
else:
    tempo(A, B)
