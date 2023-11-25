A, B, C = map(float, input().split())

try:
    delta = (B ** 2) - (4 * A * C)
    if delta > 0:
        x1 = ((-1 * B) + (delta ** 0.5)) / (2 * A)
        x2 = ((-1 * B) - (delta ** 0.5)) / (2 * A)
        print("R1 = {:.5f}".format(x1))
        print("R2 = {:.5f}".format(x2))
    else:
        print("Impossivel calcular")
except:
    print("Impossivel calcular")
