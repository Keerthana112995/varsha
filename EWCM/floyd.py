INF = float('INF')

def floyd(graph):
    v = len(graph)
    for k in range(v):
        for i in range(v):
            for j in range(v):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    return graph

graph = [
    [0, 3, INF, 5],
    [2, 0, INF, 4],
    [INF, 1, 0, INF],
    [INF, INF, 2, 0]
]

for row in floyd(graph):
    print(row)



