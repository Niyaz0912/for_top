from teacher import Teacher


def test_teacher_init():
    teacher = Teacher("test_name", "test_surname", "test_phone")
    assert len(Teacher.teachers_list)
    assert len(Teacher.phone_list)


def test_get_name(teacher):
    assert teacher.get_name() == "test_name"


def test_get_surname(teacher):
    assert teacher.get_surname() == "test_surname"


def test_get_phone(teacher):
    assert teacher.get_phone() == "test_phone"


def pay_salary(teacher):
    assert teacher.pay_salary(50000) == "работник {self.__name} {self.__surname}, получил зарплату {salary}"


def test_print_teachers_data(teacher):
    assert teacher.print_teachers_data() == "Данные успешно получены"
    assert Teacher.print_teachers_data() == "Данные успешно получены"


def test_fire_teacher(teacher):
    print(len(Teacher.teachers_list))
    assert teacher.fire_teacher() == "Сотрудник test_name test_surname был уволен"
    assert teacher.fire_teacher() == "Сотрудника test_name test_surname уже уволили"
