from typing import List


def count_platforms(weights: List[int], limit: int) -> int:
    """Функция для подсчёта минимального количества платформ для переправы.

    Args:
        weights: Список весов.
        limit: Максимальный вес, который выдерживает платформа.

    Returns:
        Количество платформ, необходимое для переправы.

    Variable:
        left_pointer, right_pointer: Переменные хранящие данные для
        сравнения с максимальным весом. Если их сумма больше limit,
        то двигаем только right_pointer, иначе обе переменные.

    """
    sorted_weights = sorted(weights)  # Создаём новый отсортированный список
    left_pointer: int = 0
    right_pointer: int = len(sorted_weights) - 1
    count: int = 0

    while left_pointer <= right_pointer:
        if sorted_weights[left_pointer] + sorted_weights[right_pointer] <= limit:
            left_pointer += 1
        right_pointer -= 1
        count += 1

    return count


# Андрей, привет. Подскажи, пожалуйста. При наведении на limit
# в диалоговом окне высвечивается комментарий опианый в докстринг.
# Это можно применять ко всему? Чтоб переменные описывать и т.д.?
# Очень удобно как на первый взгляд.
if __name__ == '__main__':
    weights = [int(weight) for weight in input().split()]
    limit = int(input())

    print(count_platforms(weights, limit))
