def find_target_index(arr, target):
    """
    Находит индекс первого вхождения целевого значения в отсортированном массиве.
    Если значение не найдено, возвращает индекс, на котором оно могло бы находиться.
    """
    left, right = 0, len(arr) - 1
    result = len(arr)  # Запоминаем индекс для вставки

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] >= target:  # Если нашли target или больший элемент
            result = mid  # Запоминаем индекс
            right = mid - 1  # Двигаемся влево
        else:
            left = mid + 1  # Двигаемся вправо

    return result  # Возвращаем первый индекс, где стоит target


arr = list(map(int, input().split()))

# Считываем целевое значение
target = int(input())

# Вызываем функцию поиска
index = find_target_index(arr, target)

# Выводим результат
print(index)