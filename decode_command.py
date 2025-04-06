# Константа, содержащая все цифры от 0 до 9
DIGITS = "0123456789"


def decode_command(encoded_string: str) -> str:
    """
    Decode_command - работает в виде внешнего инферфейса.

    Получает навход строку. Далее вызывается '_Decode' с полученой строкой
    и начальным индексом.
    """
    result, _ = _decode(encoded_string, 0)
    return result


def _decode(encoded_string: str, index: int) -> tuple[str, int]:
    """
    Decode_command - Получает на вход строку и индекс символа.

    ID успешной проверки contest - 136016593
    В цикле проверяем является ли символ числом.
    Если символ '[' то вход в рекурсию.
    Если символ ']' то выход из рекурсии и собираем строку.
    """
    result = ""
    execution_counter = 0

    while index < len(encoded_string):
        char = encoded_string[index]

        if char in DIGITS:  # Если число, записываем.
            execution_counter = execution_counter * 10 + int(char)

        elif char == '[':
            # Рекурсивный вызов.
            sub_string, index = _decode(encoded_string, index + 1)
            result += execution_counter * sub_string  # Повторяем подстроку.
            execution_counter = 0  # Обнуляем количество повторений.

        elif char == ']':
            return result, index

        # Если буква, просто добавляем.
        else:
            result += char

        # Переходим к следующему символу.
        index += 1

    return result, index


# Андрей, привет. Я тут слегка переделал по твоему примеру!
if __name__ == '__main__':
    encoded_string = input()
    print(decode_command(encoded_string))
