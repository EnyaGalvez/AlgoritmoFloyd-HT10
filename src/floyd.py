def floyd_warshall(matriz):
    n = len(matriz)
    dist = [fila[:] for fila in matriz]
    path = [[-1]*n for _ in range(n)]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    path[i][j] = k
    return dist, path