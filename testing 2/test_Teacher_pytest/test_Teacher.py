from Teacher import Teacher, DisciplineTeacher


def teacher():
    return Teacher("Иван Петров", "БГПУ", "4 года")


def discipline_teacher():
    return DisciplineTeacher("Иван Петров", "БГПУ", "4 года", "Химия", "Директор")


def test_teacher_get_teacher_data(teacher1):
    assert teacher1.get_teacher_data() == "Иван Петров, БГПУ, 4 года"


def test_teacher_add_mark(teacher1):
    assert teacher1.add_mark("Петр Сидоров", 4) == "Иван Петров поставил оценку 4 студенту Петр Сидоров"


def test_teacher_remove_mark(teacher1):
    assert teacher1.remove_mark("Дмитрий Степанов", 3) == "Иван Петров удалил оценку 3 у студента Дмитрий Степанов"


def test_teacher_give_a_consultation(teacher1):
    assert teacher1.give_a_consultation("9Б") == "Иван Петров провел консультацию в классе 9Б"


def test_discipline_teacher_get_teacher_data(discipline_teacher2):
    assert discipline_teacher2.get_teacher_data() == "Иван Петров, БГПУ, 4 года, Химия, Директор"


def test_discipline_teacher_get_discipline(discipline_teacher2):
    assert discipline_teacher2.get_discipline() == "Химия"


def test_discipline_teacher_get_job_title(discipline_teacher2):
    assert discipline_teacher2.get_job_title() == "Директор"


def test_discipline_teacher_set_job_title(discipline_teacher2):
    discipline_teacher2.set_job_title("Завуч")
    assert discipline_teacher2.get_job_title() == "Завуч"


def test_discipline_teacher_add_mark(discipline_teacher2):
    assert discipline_teacher2.add_mark("Николай Иванов",
                                       4) == "Иван Петров поставил оценку 4 студенту Николай Иванов по предмету Химия"


def test_discipline_teacher_remove_mark(discipline_teacher2):
    assert discipline_teacher2.remove_mark("Дмитрий Степанов",
                                          3) == "Иван Петров удалил оценку 3 у студента Дмитрий Степанов по предмету Химия"


def test_discipline_teacher_give_a_consultation(discipline_teacher2):
    assert discipline_teacher2.give_a_consultation(
        "10Б") == "Иван Петров провел консультацию в классе 10Б по предмету Химия как Директор"
