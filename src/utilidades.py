def reconstruir_camino(i, j, path, ciudades):
    if path[i][j] == -1:
        return []
    k = path[i][j]
    return (reconstruir_camino(i, k, path, ciudades) +
            [ciudades[k]] +
            reconstruir_camino(k, j, path, ciudades))