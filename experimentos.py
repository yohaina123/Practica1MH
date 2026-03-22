import time
import os
import matplotlib.pyplot as plt

from funcion_objetivo import funcion_objetivo
from busqueda_local import first_improvement, best_improvement


def ejecutar_experimentos(schedule, student_exam, n_slots):

    results = {}

    # FIRST IMPROVEMENT
    start = time.time()
    s1 = first_improvement(schedule, student_exam, n_slots)
    t1 = time.time() - start

    cost1 = funcion_objetivo(s1, student_exam)

    results["first_improvement"] = (cost1, t1)

    # BEST IMPROVEMENT
    start = time.time()
    s2 = best_improvement(schedule, student_exam, n_slots)
    t2 = time.time() - start

    cost2 = funcion_objetivo(s2, student_exam)

    results["best_improvement"] = (cost2, t2)

    graficar_resultados(results)

    return results


def graficar_resultados(results):

    algoritmos = list(results.keys())
    costes = [results[a][0] for a in algoritmos]
    tiempos = [results[a][1] for a in algoritmos]

    # crear carpeta si no existe
    os.makedirs("imagenes", exist_ok=True)

    # grafica de costes
    plt.figure()
    plt.bar(algoritmos, costes)
    plt.title("Comparación de coste entre algoritmos")
    plt.xlabel("Algoritmo")
    plt.ylabel("Coste")

    plt.savefig("imagenes/costes.png")
    plt.close()

    # grafica de tiempos
    plt.figure()
    plt.bar(algoritmos, tiempos)
    plt.title("Tiempo de ejecución de los algoritmos")
    plt.xlabel("Algoritmo")
    plt.ylabel("Tiempo (segundos)")

    plt.savefig("imagenes/tiempos.png")
    plt.close()