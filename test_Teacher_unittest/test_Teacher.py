import unittest
from Teacher import Teacher, DisciplineTeacher


class TestTeacher(unittest.TestCase):
    def setUp(self):
        self.teacher = Teacher("Иван Петров", "БГПУ", "4 года")

    def test_get_teacher_data(self):
        self.assertEqual(self.teacher.get_teacher_data(), "Иван Петров, БГПУ, 4 года")

    def test_add_mark(self):
        self.assertEqual(self.teacher.add_mark("Петр Сидоров", 4),
                         "Иван Петров поставил оценку 4 студенту Петр Сидоров")

    def test_remove_mark(self):
        self.assertEqual(self.teacher.remove_mark("Дмитрий Степанов", 3),
                         "Иван Петров удалил оценку 3 у студента Дмитрий Степанов")

    def test_give_a_consultation(self):
        self.assertEqual(self.teacher.give_a_consultation("9Б"), "Иван Петров провел консультацию в классе 9Б")

    def test_experience_setter(self):
        self.teacher.experience = "5 лет"
        self.assertEqual(self.teacher.experience, "5 лет")


class TestDisciplineTeacher(unittest.TestCase):
    def setUp(self):
        self.teacher = DisciplineTeacher("Иван Петров", "БГПУ", "4 года", "Химия", "Директор")

    def test_get_teacher_data(self):
        self.assertEqual(self.teacher.get_teacher_data(), "Иван Петров, БГПУ, 4 года, Химия, Директор")

    def test_get_discipline(self):
        self.assertEqual(self.teacher.get_discipline(), "Химия")

    def test_get_job_title(self):
        self.assertEqual(self.teacher.get_job_title(), "Директор")

    def test_set_job_title(self):
        self.teacher.set_job_title("Преподаватель")
        self.assertEqual(self.teacher.get_job_title(), "Преподаватель")

    def test_add_mark(self):
        self.assertEqual(self.teacher.add_mark("Николай Иванов", 4),
                         "Иван Петров поставил оценку 4 студенту Николай Иванов по предмету Химия")

    def test_remove_mark(self):
        self.assertEqual(self.teacher.remove_mark("Дмитрий Степанов", 3),
                         "Иван Петров удалил оценку 3 у студента Дмитрий Степанов по предмету Химия")

    def test_give_a_consultation(self):
        self.assertEqual(self.teacher.give_a_consultation("10Б"),
                         "Иван Петров провел консультацию в классе 10Б по предмету Химия как Директор")
