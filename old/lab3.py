import random
# 1
print("Привет, Python!")
print("Приятно познакомиться.")

# 2
film = input("Введите название фильма: ")
cinema = input("Введите название кинотеатра: ")
time = input("Введите время: ")

print(f"Билет на \"{film}\" в \"{cinema}\" на {time} забронирован.")

# 3
num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
num3 = int(input("Введите третье число: "))

sum_num = num1 + num2 + num3
num = num1 * num2 * num3
average_num = sum_num / 3

print(f"Среднее арифметическое: {average_num}")

# 4
number = random.randint(100, 999)
print(f"{number // 100}, {number % 100 // 10}, {number % 10}")

# 5
priseRub = int(input("Введите стоимость пирожка в рублях: "))
priseKap = int(input("Введите стоимость пирожка в копейках: "))
prirojki = int(input("Введите количество пирожков: "))

tpr = (priseRub + priseKap / 100) * prirojki
tpk = tpr * 100 % 100

print(f"К оплате: {int(tpr)} руб. {int(tpk)} коп.")