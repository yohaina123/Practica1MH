import random


def move_exam(schedule, exam, new_slot):

    new_schedule = schedule.copy()

    slot, room = schedule[exam]

    new_schedule[exam] = (new_slot, room)

    return new_schedule


def swap_exams(schedule, exam1, exam2):

    new_schedule = schedule.copy()

    slot1, room1 = schedule[exam1]
    slot2, room2 = schedule[exam2]

    new_schedule[exam1] = (slot2, room1)
    new_schedule[exam2] = (slot1, room2)

    return new_schedule


def generar_vecino(schedule, n_slots):

    new_schedule = schedule.copy()

    exam = random.choice(list(schedule.keys()))

    slot, room = schedule[exam]

    new_slot = random.randint(0, n_slots - 1)

    new_schedule[exam] = (new_slot, room)

    return new_schedule