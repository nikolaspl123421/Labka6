a = float(input("Введіть значення для а : "))
b = float(input('Введіть значення для b : '))
c = [float(input('Введіть значення для {0} елемента спиcку '.format(i)))for i in range(int(input('Введіть розмірність списку : ')))]
print([el for el in c if a <= el//1 <= b]+[el for el in c if el//1 <= a or el//1 >=b])