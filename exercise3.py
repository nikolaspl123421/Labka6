n = int(input('Введіть значення для n : '))
item = []
a = []
b = []
c = []
for i in range(n):
    a.append(float(input('Введіть значення для {0} елемента вектора '.format(i))))
    b.append(float(input('Введіть значення для {0} елемента вектора '.format(i))))
    c.append(float(input('Введіть значення для {0} елемента вектора '.format(i))))
for i in range(n):
    item.append((a[i]+c[i])*2-3*(a[i]-b[i]))
print(item)