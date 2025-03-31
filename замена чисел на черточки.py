def remove_duplicates(arr):
    seen = set()  # Множество для отслеживания уникальных элементов
    result = []  # Список для уникальных элементов
    duplicates = []  # Список для дубликатов

    # Перебираем элементы массива
    for num in arr:
        if num not in seen:
            seen.add(num)
            result.append(num)  # Добавляем уникальный элемент в начало
        else:
            duplicates.append('_')  # Заменяем дубликаты на "_"

    # Возвращаем массив, в котором уникальные элементы идут первыми, а затем символы "_"
    return result + duplicates


# Чтение данных с консоли
n = int(input())  # Считываем размер массива
arr = list(map(int, input().split()))  # Считываем массив целых чисел

# Обрабатываем массив и выводим результат
result = remove_duplicates(arr)
print(*result)
