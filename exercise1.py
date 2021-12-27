#Дано n є N, x, y, є R^n. Побудувати вектор z, який містить спочатку додатні координати вектора x а потім додатні координати вектора y
#Позначеня
# x - float змінна
# y - float змінна
# Введення
n = int(input("Введіть розмірність вектора: "))
x = []
y = []
z = []
for i in range(n):
    x.append(float(input('Введіть {0}-ий елемент вектора {1} '.format(i, "x"))))
    y.append(float(input('Введіть {0}-ий елемент вектора {1} '.format(i, "y"))))
for i in x:
    if i > 0:
        z.append(i)
for i in y:
    if i > 0:
        z.append(i)
print(z)
