class Teacher:
    teachers_list = []
    phone_list = []

    def __init__(self, name, surname, phone):
        self.__name = name
        self.__surname = surname
        self.__phone = phone
        Teacher.teachers_list.append(self)
        Teacher.phone_list.append(self.__phone)

    def get_name(self):
        return self.__name

    def get_surname(self):
        return self.__surname

    def get_phone(self):
        return self.__phone

    def pay_salary(self, salary):
        return f"работник {self.__name} {self.__surname}, получил зарплату {salary}"

    @staticmethod
    def print_teachers_data():
        for teacher in Teacher.teachers_list:
            print(teacher.get_name())
            print(teacher.get_surname())
            print(teacher.get_phone())
            print()
            return "Данные успешно получены"

    def fire_teacher(self):
        if self in self.teachers_list:
            self.teachers_list.remove(self)
            return f"Сотрудник {self.__name} {self.__surname} был уволен"
        else:
            return f"Сотрудника {self.__name} {self.__surname} уже уволили"


"""Создаем экземпляры класса"""
if __name__ == "__main__":
    teacher1 = Teacher("Иван", "Смирнов", "+79511234567")
    teacher2 = Teacher("Сергей", "Пермяков", "+79665437678")

    print(len(Teacher.teachers_list))
    print(Teacher.teachers_list)
    print(len(Teacher.phone_list))
    print(Teacher.phone_list)
    Teacher.print_teachers_data()
    print(teacher1.pay_salary(50000))
    print(teacher2.pay_salary(80000))
    print(teacher1.fire_teacher())
    print(len(Teacher.teachers_list))
    Teacher.print_teachers_data()
