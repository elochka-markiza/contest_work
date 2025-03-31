def valid_mountain_array(arr):
    if len(arr) < 3:
        return False

    # Ищем вершину
    peak_index = 0
    while peak_index + 1 < len(arr) and arr[peak_index] < arr[peak_index + 1]:
        peak_index += 1

    # Проверяем, что вершина не на краю
    if peak_index == 0 or peak_index == len(arr) - 1:
        return False

    # Проверяем убывающую часть
    while peak_index + 1 < len(arr) and arr[peak_index] > arr[peak_index + 1]:
        peak_index += 1

    return peak_index == len(arr) - 1


# Чтение данных с консоли
arr = list(map(int, input().split()))  # Считываем массив целых чисел

# Обрабатываем массив и выводим результат
result = valid_mountain_array(arr)
print(result)
