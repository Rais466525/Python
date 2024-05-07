# 2
year = int(input("Введите год: "))
def isLeapYear(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
def daysInYear(year):
    return 366 if isLeapYear(year) else 365
print("Количество дней в", year, "году составляет", daysInYear(year))

# 3
totalPrice = float(input("Введите общую стоимость покупки: "))
def calcDisCount(totalPrice):
    disCount = 0.05 if totalPrice > 1000 else (0.03 if totalPrice > 500 else 0)
    disCountPrice = totalPrice - (totalPrice * disCount)
    return disCountPrice
final_price = calcDisCount(totalPrice)
print(f"Итоговая стоимость с учетом скидки: {final_price}")

# 4
unit = int(input("Введите номер единицы измерения\n1 — килограмм, \n2 — миллиграмм, \n3 — грамм, \n4 — тонна, \n5 — центнер): "))
mass = float(input("\nВведите массу: "))

def toKg(unit, mass):
    if unit == 1:  # килограмм
        return mass
    if unit == 2:  # миллиграмм
        return mass / 1000000
    if unit == 3:  # грамм
        return mass / 1000
    if unit == 4:  # тонна
        return mass * 1000
    else:          # центнер
        return mass * 100

result = toKg(unit, mass)
print(f"Масса в килограммах: {result} кг")

# 5
import math
num = [float(input()) for _ in range(4)]
minNum = min(num)
cosinus = math.cos(minNum)
print(cosinus)

# 6
import math
num = [float(input()) for _ in range(3)]
maxNum = max(num)
sinus = math.sin(maxNum)
print(sinus)