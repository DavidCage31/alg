from collections import defaultdict

def dijkstra_with_buckets(graph, start):
    n = len(graph)

    distances = [float("inf")] * n
    distances[start] = 0

    visited = [False] * n

    buckets = defaultdict(set)
    buckets[0].add(start)
    current_bucket = 0
    max_bucket = 0

    while current_bucket <= max_bucket:
        # Пропускаем пустые черпаки
        while current_bucket <= max_bucket and not buckets[current_bucket]:
            current_bucket += 1
        
        if current_bucket > max_bucket:
            break

        # Обрабатываем текущий черпак
        while buckets[current_bucket]:
            vertex = buckets[current_bucket].pop()
            if visited[vertex]:
                continue

            visited[vertex] = True

            for neighbor, weight in graph[vertex]:
                if not visited[neighbor]:
                    new_dist = distances[vertex] + weight
                    if new_dist < distances[neighbor]:
                        old_dist = distances[neighbor]
                        distances[neighbor] = new_dist
                        if old_dist != float("inf"):
                            buckets[old_dist].discard(neighbor)
                        buckets[new_dist].add(neighbor)
                        if new_dist > max_bucket:
                            max_bucket = new_dist
        current_bucket += 1

    return distances

# Пример графа в виде списка смежности
graph = {
    0: [(1, 1), (2, 3)],
    1: [(2, 1)],
    2: [(3, 2)],
    3: []
}
start_vertex = 0

distances = dijkstra_with_buckets(graph, start_vertex)
print("Кратчайшие расстояния от вершины", start_vertex)
for i, d in enumerate(distances):
    print(f"До вершины {i}: {d}")
