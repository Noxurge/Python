N = int(input())
lista = []
 
for i in range(N):
    A, B, C = map(float, input().split())
    MEDIA = ((A * 2) + (B * 3) + (C * 5)) / 10
    lista.append(MEDIA)

for media in lista:
    print("{:.1f}".format(media))
