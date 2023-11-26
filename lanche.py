A, B = map(int, input().split())
codes = {1: 4, 2: 4.5, 3: 5, 4: 2, 5: 1.5}

def decisao(option, value):
    if option in codes:
        value *= codes[option]
        print("Total: R$ {:.2f}".format(float(value)))

decisao(A, B)
