I = 0
J = 1
Z = 0

while I <= 2:
    for x in range(3):
        if I == 0 or I == 1:
            print('I={:.0f} J={:.0f}'.format(I, J + I))
        elif Z == 10:
            I = 2
            print('I={:.0f} J={:.0f}'.format(I, J + I))
        else:
            print('I={:.1f} J={:.1f}'.format(I, J + I))
        J += 1
    I += 0.2
    J = 1
    Z += 1
