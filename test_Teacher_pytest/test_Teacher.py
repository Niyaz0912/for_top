from Teacher import Teacher, DisciplineTeacher


class TestTeacher:
    def test_get_teacher_data(self):
        teacher = Teacher("Иван Петров", "БГПУ", "4 года")
        assert teacher.get_teacher_data() == "Иван Петров, БГПУ, 4 года"

    def test_add_mark(self):
        teacher = Teacher("Иван Петров", "БГПУ", "4 года")
        assert teacher.add_mark("Петр Сидоров", 4) == "Иван Петров поставил оценку 4 студенту Петр Сидоров"

    def test_remove_mark(self):
        teacher = Teacher("Иван Петров", "БГПУ", "4 года")
        assert teacher.remove_mark("Дмитрий Степанов", 3) == "Иван Петров удалил оценку 3 студенту Дмитрий Степанов"

    def test_give_a_consultation(self):
        teacher = Teacher("Иван Петров", "БГПУ", "4 года")
        assert teacher.give_a_consultation("9Б") == "Иван Петров провел консультацию в классе 9Б"


class TestDisciplineTeacher:
    def test_get_teacher_data(self):
        teacher = DisciplineTeacher("Иван Петров", "образование БГПУ", " опыт работы 4 года", "предмет Химия",
                                    "должность Директор")
        assert teacher.get_teacher_data() == ("Иван Петров, образование БГПУ, опыт работы 4 года, предмет Химия, "
                                              "должность Директор")

    def test_add_mark(self):
        teacher = DisciplineTeacher("Иван Петров", "образование БГПУ", " опыт работы 4 года", "предмет Химия",
                                    "должность Директор")
        assert teacher.add_mark("Николай Иванов", 4,
                                "Предмет: Химия") == ("Иван Петров поставил оценку 4 студенту Николай "
                                                      "Иванов.\nПредмет: Химия")

    def test_remove_mark(self):
        teacher = DisciplineTeacher("Иван Петров", "образование БГПУ", " опыт работы 4 года", "предмет Химия",
                                    "должность Директор")
        assert teacher.remove_mark("Дмитрий Степанов", 3,
                                   "Предмет: Химия") == ("Иван Петров удалил оценку 3 студенту Дмитрий "
                                                         "Степанов.\nПредмет: Химия")

    def test_give_a_consultation(self):
        teacher = DisciplineTeacher("Иван Петров", "образование БГПУ", " опыт работы 4 года", "предмет Химия",
                                    "должность Директор")
        assert teacher.give_a_consultation("10Б", "предмету Химия",
                                           "Директор") == ("Иван Петров провел консультацию в классе 10Б.\nПо предмету "
                                                           "Химия как Директор")
