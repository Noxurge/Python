quantidade = int(input())
inside = 0
outside = 0

if quantidade < 10000:
    for i in range(quantidade):
        x = int(input())
        if -10 ** 7 < x < 10 ** 7:
            if x in range(10, 20):
                inside += 1
            else:
                outside += 1

print("{} in\n{} out".format(inside, outside))
