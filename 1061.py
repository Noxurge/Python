dia_i = int(input().split()[1])
hora_i, minuto_i, segundo_i = map(int, input().split(" : "))
dia_f = int(input().split(" ")[1])
hora_f, minuto_f, segundo_f = map(int, input().split(" : "))

inicio_segundos = (dia_i - 1) * 86400 + hora_i * 3600 + minuto_i * 60 + segundo_i
termino_segundos = (dia_f - 1) * 86400 + hora_f * 3600 + minuto_f * 60 + segundo_f

diferenca_segundos = termino_segundos - inicio_segundos

dias = diferenca_segundos // 86400
diferenca_segundos = diferenca_segundos % 86400
horas = diferenca_segundos // 3600
diferenca_segundos = diferenca_segundos % 3600
minutos = diferenca_segundos // 60
segundos = diferenca_segundos % 60

print("{} dia(s)".format(dias))
print("{} hora(s)".format(horas))
print("{} minuto(s)".format(minutos))
print("{} segundo(s)".format(segundos))
