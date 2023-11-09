
def dijkstra(graph, start):
    # Инициализация словарей для хранения расстояний и предшественников
    distances = {vertex: float('infinity') for vertex in graph}
    predecessors = {vertex: None for vertex in graph}
    distances[start] = 0
    # Итерация по вершинам
    while graph:
        # Выбираем вершину с наименьшим расстоянием
        current_vertex = min(distances, key=distances.get)

        # Итерируемся по соседям текущей вершины
        for neighbor, weight in graph[current_vertex].items():
            potential_distance = distances[current_vertex] + weight
            # Если найден более короткий путь, обновляем расстояние и предшественника
            if potential_distance < distances[neighbor]:
                distances[neighbor] = potential_distance
                predecessors[neighbor] = current_vertex
        
        # Удаляем обработанную вершину из графа
        del distances[current_vertex]

    return distances, predecessors
