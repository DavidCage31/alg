import heapq

class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, element):
        heapq.heappush(self.heap, element)

    def extract_min(self):
        return heapq.heappop(self.heap)

    def get_min(self):
        return self.heap[0] if self.heap else None

    def is_empty(self):
        return len(self.heap) == 0

# Пример использования
min_heap = MinHeap()
min_heap.insert(5)
min_heap.insert(3)
min_heap.insert(8)

print(min_heap.get_min())       # 3
print(min_heap.extract_min())   # 3
print(min_heap.get_min())       # 5

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
