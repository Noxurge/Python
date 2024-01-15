N = int(input())

for i in range(N):
    X,Y = map(int, input().split())
    try:
        calc = X/Y
        print(f"{calc}")
    except:
        print("divisao impossivel")
