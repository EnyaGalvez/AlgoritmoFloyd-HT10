def eliminar_conexion(grafo, ciudad1, ciudad2):
    if ciudad1 in grafo.indices and ciudad2 in grafo.indices:
        i, j = grafo.indices[ciudad1], grafo.indices[ciudad2]
        for clima in grafo.matrices:
            grafo.matrices[clima][i][j] = float('inf')
    else:
        print("Una o ambas ciudades no existen.")


def agregar_conexion(grafo, ciudad1, ciudad2, tiempos):
    for ciudad in [ciudad1, ciudad2]:
        if ciudad not in grafo.indices:
            grafo.ciudades.append(ciudad)
            grafo.indices[ciudad] = len(grafo.ciudades) - 1
            for clima in grafo.matrices:
                for fila in grafo.matrices[clima]:
                    fila.append(float('inf'))
                grafo.matrices[clima].append([float('inf')] * len(grafo.ciudades))
                grafo.matrices[clima][-1][-1] = 0

    i, j = grafo.indices[ciudad1], grafo.indices[ciudad2]
    for clima, tiempo in tiempos.items():
        grafo.matrices[clima][i][j] = tiempo


def cambiar_clima(grafo, clima):
    if clima in grafo.matrices:
        grafo.clima_activo = clima
    else:
        print("Clima no válido.")