import heapq

# Создание пустой кучи
min_heap = []

# Вставка элементов
heapq.heappush(min_heap, 5)
heapq.heappush(min_heap, 3)
heapq.heappush(min_heap, 8)

# Получение минимального элемента
print("Минимальный элемент:", min_heap[0])  # 3

# Извлечение минимального элемента
print("Извлеченный элемент:", heapq.heappop(min_heap))  # 3
print("Минимальный элемент после извлечения:", min_heap[0])  # 5

# Вставка еще одного элемента
heapq.heappush(min_heap, 2)
print("Минимальный элемент после вставки 2:", min_heap[0])  # 2


def dijkstra(graph, start):
    # Инициализация расстояний
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    priority_queue = [(0, start)]  # (расстояние, вершина)

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Если расстояние больше, чем уже найденное, пропускаем
        if current_distance > distances[current_vertex]:
            continue

        # Обновление соседей
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # Если найдено более короткое расстояние
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Пример графа
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

# Запуск алгоритма
shortest_paths = dijkstra(graph, 'A')
print(shortest_paths)  # {'A': 0, 'B': 1, 'C': 3, 'D': 4}
