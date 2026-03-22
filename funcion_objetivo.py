from collections import defaultdict

def funcion_objetivo(schedule, student_exam):

    penalty = 0

    student_slots = defaultdict(list)

    for _, row in student_exam.iterrows():

        student = row["student"]
        exam = row["exam"]

        if exam in schedule:
            slot, _ = schedule[exam]
            student_slots[student].append(slot)

    for student, slots in student_slots.items():

        slots.sort()

        for i in range(len(slots)-1):

            if slots[i+1] == slots[i]:
                penalty += 100

            if slots[i+1] == slots[i] + 1:
                penalty += 5

    return penalty