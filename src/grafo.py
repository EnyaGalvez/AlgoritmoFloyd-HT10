from floyd import floyd_warshall
from utilidades import reconstruir_camino

class Grafo:
    def __init__(self):
        self.ciudades = []
        self.indices = {}
        self.matrices = {
            "normal": [],
            "lluvia": [],
            "nieve": [],
            "tormenta": []
        }

    def cargar_desde_archivo(self, archivo):
        with open(archivo, 'r') as f:
            lineas = f.readlines()[1:]

        conexiones = []
        for linea in lineas:
            datos = linea.strip().split()
            c1, c2 = datos[0], datos[1]
            tiempos = list(map(float, datos[2:]))
            if c1 not in self.ciudades:
                self.ciudades.append(c1)
            if c2 not in self.ciudades:
                self.ciudades.append(c2)
            conexiones.append((c1, c2, tiempos))

        self.indices = {ciudad: i for i, ciudad in enumerate(self.ciudades)}
        n = len(self.ciudades)
        for clima in self.matrices:
            self.matrices[clima] = [[float('inf')] * n for _ in range(n)]
            for i in range(n):
                self.matrices[clima][i][i] = 0

        for c1, c2, tiempos in conexiones:
            i, j = self.indices[c1], self.indices[c2]
            for idx, clima in enumerate(["normal", "lluvia", "nieve", "tormenta"]):
                self.matrices[clima][i][j] = tiempos[idx]

    def obtener_ruta(self, origen, destino, clima="normal"):
        dist, path = floyd_warshall(self.matrices[clima])
        i, j = self.indices[origen], self.indices[destino]
        camino = [origen] + reconstruir_camino(i, j, path, self.ciudades) + [destino]
        return dist[i][j], camino

    def calcular_centro(self, clima="normal"):
        dist, _ = floyd_warshall(self.matrices[clima])
        exc = [max(fila) for fila in dist]
        return self.ciudades[exc.index(min(exc))]