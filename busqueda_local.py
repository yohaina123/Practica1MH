from funcion_objetivo import funcion_objetivo
from vecinos import generar_vecino


def first_improvement(schedule, student_exam, n_slots, max_iter=30):

    current = schedule
    current_cost = funcion_objetivo(current, student_exam)

    # máximo de iteraciones globales
    for _ in range(200):

        improved = False

        for _ in range(max_iter):

            neighbor = generar_vecino(current, n_slots)

            cost = funcion_objetivo(neighbor, student_exam)

            if cost < current_cost:

                current = neighbor
                current_cost = cost
                improved = True
                break

        # criterio de parada: si no hay mejora
        if not improved:
            break

    return current


def best_improvement(schedule, student_exam, n_slots, vecinos=30):

    current = schedule
    best_cost = funcion_objetivo(current, student_exam)

    for _ in range(vecinos):

        neighbor = generar_vecino(current, n_slots)

        cost = funcion_objetivo(neighbor, student_exam)

        if cost < best_cost:

            best_cost = cost
            current = neighbor

    return current