import sys
import os
sys.path.append(os.path.abspath(".."))

from grafo import Grafo

def test_centro():
    grafo = Grafo()
    grafo.cargar_desde_archivo("logistica.txt")
    centro = grafo.calcular_centro("normal")
    print("Centro del grafo:", centro)

def test_ruta():
    grafo = Grafo()
    grafo.cargar_desde_archivo("logistica.txt")
    tiempo, ruta = grafo.obtener_ruta("Tokyo", "Singapore", "lluvia")
    print("Tiempo:", tiempo)
    print("Ruta:", " -> ".join(ruta))

def test_ruta_con_clima_activo():
    grafo = Grafo()
    grafo.cargar_desde_archivo("logistica.txt")
    grafo.clima_activo = "nieve"
    tiempo, ruta = grafo.obtener_ruta("Seoul", "Jakarta")
    print("Tiempo (nieve):", tiempo)
    print("Ruta:", " -> ".join(ruta))

if __name__ == "__main__":
    test_centro()
    test_ruta()
    test_ruta_con_clima_activo()