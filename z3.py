lower = int(input("Введите первое число массива"))
upper = int(input("Введите последнее число массива"))
n = 3
for i in range (lower, upper +1):
    if (i % n == 0):
        print(i)
