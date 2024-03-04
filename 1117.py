while True:
    try:
        a = float(input())
        if 0 <= a <= 10:
            break
        else:
            print("nota invalida")
    except:
        print("nota invalida")

while True:
    try:
        b = float(input())
        if 0 <= b <= 10:
            break
        else:
            print("nota invalida")
    except:
        print("nota invalida")

calc = (a + b) / 2
print(f"media = {calc:.2f}")
