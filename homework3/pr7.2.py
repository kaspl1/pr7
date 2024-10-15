# Функция для перевода числа в 13-ю систему счисления (рекурсивная)
def to_base13(n):
    digits = "0123456789ABC"  # Числа от 0 до 12 представлены символами 0-9, A, B, C
    if n == 0:
        return ''
    return to_base13(n // 13) + digits[n % 13]

def main():
    try:
        num = int(input("Введите целое десятичное число: "))

        if num == 0:
            print("Число в 13-й системе счисления: 0")
        elif num > 0:
            print(f"Число в 13-й системе счисления: {to_base13(num)}")
        else:
            # Для отрицательных чисел добавляем знак перед результатом
            print(f"Число в 13-й системе счисления: -{to_base13(abs(num))}")

    except Exception as e:
        print("Ошибка: ввод не верный.")

if __name__ == "__main__":
    main()
