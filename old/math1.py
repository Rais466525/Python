print('Здавстуйте!')
a = int(input('Ведите число a: '))
b = int(input('Ведите чило b: '))

option = input('Выбирите операцию:\n 1) Плюс\n 2) Минус\n 3) Деление\n 4) Умножение\n')

# Проверка опции
if option == "1":
   resualt = a+b
if option == "2":
   resualt = a-b
if option == "3":
   resualt = a/b
if option == "4":
   resualt = a*b

# Результаты
print(resualt)