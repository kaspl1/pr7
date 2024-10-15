def main():
    try:
        num = int(input("Введите целое десятичное число: "))
        if num >= 0:
            print(f"Двоичное представление: {bin(num)[2:]}")
            print(f"Восьмеричное представление: {oct(num)[2:]}")
        else:
            print(f"Двоичное представление: -{bin(abs(num))[2:]}")
            print(f"Восьмеричное представление: -{oct(abs(num))[2:]}")

    except Exception as e:
        print("Ошибка: ввод не верный.")


if __name__ == "__main__":
    main()
