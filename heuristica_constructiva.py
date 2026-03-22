import random


def solucion_inicial(exams, rooms, n_slots):

    schedule = {}

    exams_sorted = exams.sort_values(by="n_students", ascending=False)

    for _, exam in exams_sorted.iterrows():

        exam_id = exam["exam"]
        students = exam["n_students"]

        posibles_rooms = rooms[rooms["capacity"] >= students]["room"].tolist()

        if not posibles_rooms:
            continue

        slot = random.randint(0, n_slots - 1)
        room = random.choice(posibles_rooms)

        schedule[exam_id] = (slot, room)

    return schedule