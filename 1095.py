i = 1
J = 60

for i in range(i, J, 3):
    print("I={} J={}".format(i, J))
    J -= 5
    if J < 0:
        break
