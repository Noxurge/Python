N = float(input())
intervalo = ["[0,25]", "(25,50]", "(50,75]", "(75,100]"]

if 0 < N <= 25:
    print("Intervalo {}".format(intervalo[0]))
elif 25.00001 < N <= 50:
    print("Intervalo {}".format(intervalo[1]))
elif 50.00001 < N <= 75:
    print("Intervalo {}".format(intervalo[2]))
elif 75.00001 < N <= 100:
    print("Intervalo {}".format(intervalo[3]))
else:
    print("Fora de intervalo")
