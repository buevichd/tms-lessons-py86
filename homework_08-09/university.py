from student import Student
from functools import reduce

students = [
    Student('A', 6),
    Student('B', 7),
    Student('C', 8),
    Student('D', 9),
    Student('E', 10),
]


def calc_sum_scholarship(sl: list[Student]) -> float:
    result = 0
    for s in sl:
        result += s.get_scholarship()
    return result

    # return reduce(lambda x, y: x + y.get_scholarship(), sl, 0)
    #
    # return sum([s.get_scholarship() for s in sl])


print(calc_sum_scholarship(students))



def get_excellent_student_count(sl: list[Student]):
    # counter = 0
    # for s in sl:
    #     if s.is_excellent():
    #         counter += 1
    # return counter

    return len(list(filter(Student.is_excellent, sl)))
