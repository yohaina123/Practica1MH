from generador_instancias import generar_instancia
from heuristica_constructiva import solucion_inicial
from funcion_objetivo import funcion_objetivo
from experimentos import ejecutar_experimentos


def main():

    # Genera instancia del problema
    student_exam, exams, rooms, n_slots = generar_instancia()

    # Crearmos solución inicial con la heurística constructiva
    schedule = solucion_inicial(exams, rooms, n_slots)

    # Mostramos información inicial
    print("\nInstancia generada")
    print("----------------------")
    print("Numero de examenes:", len(schedule))
    print("Numero de slots:", n_slots)

    # Calculamos coste inicial
    coste_inicial = funcion_objetivo(schedule, student_exam)

    print("\nCoste inicial:", coste_inicial)

    # Ejecutmoss experimentos
    results = ejecutar_experimentos(schedule, student_exam, n_slots)

    # Mostramos los resultados
    print("\nResultados")
    print("----------------------")

    for alg, (cost, tiempo) in results.items():

        print(f"{alg}")
        print(f"Coste final: {cost}")
        print(f"Tiempo: {tiempo:.2f} segundos\n")


if __name__ == "__main__":
    main()