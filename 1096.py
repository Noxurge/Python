J = 7
i = 1

for i in range(i, 10, 2):
    for rep in range(3):
        if J == 4:
            J = 7
        print("I={} J={}".format(i, J))
        J -= 1
