def josephus_problem(n, k):
    # Инициализируем список претендентов с номерами от 1 до n
    circle = list(range(1, n + 1))
    removed_numbers = []  # Список для хранения выбывших чисел
    
    # Начальный индекс для выбывающего претендента
    index = 0
    
    # Пока в круге больше одного претендента, продолжаем отсев
    while len(circle) > 1:
        # Находим индекс претендента, который выбывает
        index = (index + k - 1) % len(circle)
        
        # Добавляем выбывшего претендента в список удалённых
        removed_numbers.append(circle.pop(index))
    
    # Возвращаем оставшегося претендента и список удалённых
    return circle[0], removed_numbers


if __name__ == '__main__':
    # Вводим количество претендентов (N) и количество тактов (K)
    n = int(input())
    k = int(input())
    
    # Находим победителя и выбывших
    winner, removed = josephus_problem(n, k)
    
    # Выводим номер победителя и выбывших
    print(winner)
  
