def validate_input(permanence_period, target_time):
    if not isinstance(permanence_period, list):
        return False
    if not all(
        isinstance(tupla, tuple) and all(isinstance(i, int) for i in tupla)
        for tupla in permanence_period
    ):
        return False
    if not isinstance(target_time, int):
        return False
    return True


def study_schedule(permanence_period, target_time):
    if not validate_input(permanence_period, target_time):
        return None
    c = 0
    for student_time in permanence_period:
        if student_time[0] <= target_time <= student_time[1]:
            c += 1
    return c
