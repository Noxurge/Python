N = int(input())

if 5 < N < 2000:
    for NUM in range(1, (N + 1)):
        if NUM % 2 == 0:
            A = NUM ** 2
            print("{}^2 = {}".format(NUM, A))
