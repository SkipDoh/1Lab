import random
number = random.randint(100, 999)
print("Сгенерированное трехзначное число:", number)
digits = [int(digit) for digit in str(number)]
print("Цифры числа через запятую:", ", ".join(map(str, digits)))