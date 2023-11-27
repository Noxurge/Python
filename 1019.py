N = int(input())
hour = N // 3600
N %= 3600
minut = N // 60
N %= 60

print("{}:{}:{}".format(hour, minut, N))
