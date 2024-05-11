def is_prime(num):
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def main():
    while True:
        try:
            num = int(input("Введите число (от 2 до 100000): "))
            if num < 2 or num > 100000:
                print("Число должно быть от 2 до 100000. Попробуйте еще раз.")
                continue
            break
        except ValueError:
            print("Ошибка! Введите целое число.")

    if is_prime(num):
        print(f"{num} является простым числом.")
    else:
        print(f"{num} является составным числом.")

if __name__ == "__main__":
    main()
