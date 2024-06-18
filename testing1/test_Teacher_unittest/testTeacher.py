import unittest
from teacher import Teacher


# class TestTeacher(unittest.TestCase):
#     teacher = Teacher('test_name', 'test_surname', 'test_phone')
#
#     def test_1_init(self):
#         self.assertEqual(len(Teacher.teachers_list), 1)
#         self.assertEqual(Teacher.teachers_list, {'test_phone': ['test_name', 'test_surname']})
#
#     def test_2_get_name(self):
#         self.assertEqual(self.teacher.get_name(), 'test_name')
#
#     def test_2_get_surname(self):
#         self.assertEqual(self.teacher.get_surname(), 'test_surname')
#
#     def test_2_get_phone(self):
#         self.assertEqual(self.teacher.get_phone(), 'test_phone')
#
#     def test_5_pay_salary(self):
#         self.assertEqual(self.teacher.pay_salary(50000),
#                          'работник {self.__name} {self.__surname}, получил зарплату {salary}')


class TestTeacher(unittest.TestCase):
    def setUp(self):
        self.teacher1 = Teacher("Иван", "Смирнов", "+79511234567")
        self.teacher2 = Teacher("Сергей", "Пермяков", "+79665437678")

    def test_init(self):
        self.assertEqual(self.teacher1.get_name(), "Иван")
        self.assertEqual(self.teacher1.get_surname(), "Смирнов")
        self.assertEqual(self.teacher1.get_phone(), "+79511234567")

    def test_pay_salary(self):
        self.assertEqual(self.teacher1.pay_salary(50000), "работник Иван Смирнов, получил зарплату 50000")
        self.assertEqual(self.teacher2.pay_salary(80000), "работник Сергей Пермяков, получил зарплату 80000")

    def test_fire_teacher(self):
        self.assertEqual(self.teacher1.fire_teacher(), "Сотрудник Иван Смирнов был уволен")
        self.assertEqual(self.teacher2.fire_teacher(), "Сотрудник Сергей Пермяков был уволен")

    def test_print_teachers_data(self):
        self.assertEqual(Teacher.print_teachers_data(), "Данные успешно получены")

    def test_phone_list(self):
        self.assertEqual(len(Teacher.phone_list), 8)
        self.assertIn("+79511234567", Teacher.phone_list)
        self.assertIn("+79665437678", Teacher.phone_list)

    def test_teachers_list(self):
        self.assertEqual(len(Teacher.teachers_list), 10)
        self.assertIn(self.teacher1, Teacher.teachers_list)
        self.assertIn(self.teacher2, Teacher.teachers_list)

if __name__ == "__main__":
    unittest.main()