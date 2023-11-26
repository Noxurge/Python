A, B, C, D = map(float, input().split())
media = [2, 3, 4, 1]
def calc(value, value1, value2, value3):
    result = (value * media[0] + value1 * media[1] + value2 * media[2] + value3 * media[3]) / 10
    print("Media: {:.1f}".format(result))
    if 5 <= result <= 6.9:
        print("Aluno em exame.")
        exam = float(input())
        result = (result + exam) / 2
        print("Nota do exame: {:.1f}".format(exam))
        if result >= 5:
            print("Aluno aprovado.")
        else:
            print("Aluno reprovado.")
        print("Media final: {:.1f}".format(result))
    elif result >= 7:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")

calc(A, B, C, D)
