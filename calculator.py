def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Ошибка: деление на ноль"
    return a / b

while True:
    print("\nКалькулятор")
    print("1 - Сложение")
    print("2 - Вычитание")
    print("3 - Умножение")
    print("4 - Деление")
    print("0 - Выход")

    choice = input("Выбор: ")

    if choice == "0":
        break

    a = float(input("Первое число: "))
    b = float(input("Второе число: "))

    if choice == "1":
        print("Результат:", add(a, b))
    elif choice == "2":
        print("Результат:", sub(a, b))
    elif choice == "3":
        print("Результат:", mul(a, b))
    elif choice == "4":
        print("Результат:", div(a, b))
    else:
        print("Неверный выбор")
