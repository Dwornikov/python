from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
MAX_ATTEMPTS = 10

def guess_number():
    # Загадываем случайное число
    secret_number = randint(LOWER_LIMIT, UPPER_LIMIT)

    print("Программа загадала число от 0 до 1000. У вас есть 10 попыток, чтобы его угадать.")

    for attempt in range(1, MAX_ATTEMPTS + 1):
        try:
            guess = int(input(f"Попытка №{attempt}: Введите ваше предположение: "))
        except ValueError:
            print("Ошибка! Введите целое число.")
            continue

        if guess < LOWER_LIMIT or guess > UPPER_LIMIT:
            print(f"Число должно быть от {LOWER_LIMIT} до {UPPER_LIMIT}. Попробуйте еще раз.")
            continue

        if guess < secret_number:
            print("Больше.")
        elif guess > secret_number:
            print("Меньше.")
        else:
            print(f"Поздравляем! Вы угадали число {secret_number} за {attempt} попыток!")
            return

    print(f"К сожалению, вы исчерпали все попытки. Загаданное число было: {secret_number}.")

if __name__ == "__main__":
    guess_number()
