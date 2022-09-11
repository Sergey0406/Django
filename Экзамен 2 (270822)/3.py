# № 3
try:
    num_1 = int and float(input("Введите делимое: "))
    num_2 = int and float(input("Введите делитель: "))
    result = num_1 / num_2
    print("Частное равно", result)
except ValueError:
    print("Ошибка при вводе числа!")
except ZeroDivisionError:
    result = 0
    print("Частное равно 0.")
finally:
    print("Программа завершена.")