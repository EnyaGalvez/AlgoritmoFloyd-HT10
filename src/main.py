from grafo import Grafo

from modificador import (
    eliminar_conexion,
    agregar_conexion,
    cambiar_clima
)

def main():
    grafo = Grafo()
    grafo.cargar_desde_archivo("logistica.txt")

    while True:
        print("\nMenú:")
        print("1. Consultar ruta más corta")
        print("2. Calcular ciudad centro del grafo")
        print("3. Modificar grafo")
        print("4. Salir")
        op = input("Opción: ")

        if op == "1":
            origen = input("Ciudad origen: ")
            destino = input("Ciudad destino: ")
            clima = input("Clima (normal, lluvia, nieve, tormenta): ")
            tiempo, ruta = grafo.obtener_ruta(origen, destino, clima)
            print("Tiempo:", tiempo)
            print("Ruta:", " -> ".join(ruta))
        elif op == "2":
            clima = input("Clima (normal, lluvia, nieve, tormenta): ")
            print("Centro del grafo:", grafo.calcular_centro(clima))
        elif op == "3":
            print("\nOpciones de modificación:")
            print("a. Interrupción de tráfico entre dos ciudades")
            print("b. Establecer nueva conexión entre dos ciudades")
            print("c. Modificar el clima activo")
            sub_op = input("Seleccione opción (a, b, c): ").lower()

            if sub_op == "a":
                ciudad1 = input("Ciudad 1: ")
                ciudad2 = input("Ciudad 2: ")
                eliminar_conexion(grafo, ciudad1, ciudad2)

            elif sub_op == "b":
                ciudad1 = input("Ciudad 1: ")
                ciudad2 = input("Ciudad 2: ")
                tiempos = {}
                for clima in ["normal", "lluvia", "nieve", "tormenta"]:
                    tiempos[clima] = float(input(f"Tiempo en clima {clima}: "))
                agregar_conexion(grafo, ciudad1, ciudad2, tiempos)

            elif sub_op == "c":
                clima = input("Nuevo clima activo (normal, lluvia, nieve, tormenta): ").lower()
                cambiar_clima(grafo, clima)
        elif op == "4":
            break

if __name__ == "__main__":
    main()