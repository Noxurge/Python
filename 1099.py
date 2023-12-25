N = int(input())
x = 0
y = 0

for i in range(N):
    X, Y = map(int, input().split())
    if X < Y:
        for a in range(X + 1, Y):
            if a % 2 != 0:
                x += a
        print(x)
        x = 0
    elif X > Y:
        lista2 = []
        for a in range(Y + 1, X):
            if a % 2 != 0:
                y += a
        print(y)
        y = 0
    elif X == Y:
        print(0)
