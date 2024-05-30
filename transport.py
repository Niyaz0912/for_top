class Vehicle:
    """Создан класс Vehicle с атрибутами марка и пробег"""
    def __init__(self, name, mileage):
        self.name = name
        self.mileage = mileage

    def get_vehicle_type(self, wheels):
        """Через данный метод по количеству колес определяем тип ТС"""
        if wheels == 2:
            return f"Это мотоцикл марки {self.name}."
        elif wheels == 3:
            return f"Это трицикл марки {self.name}."
        elif wheels == 4:
            return f"Это автомобиль марки {self.name}."
        else:
            return f"Я не знаю таких ТС."

    def get_vehicle_advice(self):
        """Данный метод в зависимости от пробега дает рекомендации пользователю,
        можно ли преобретать данное ТС"""
        if self.mileage < 50000:
            return f"Неплохо {self.name} можно брать."
        elif 50001 <= self.mileage <= 100000:
            return f"{self.name} надо внимательно проверить."
        elif 100001 <= self.mileage <= 150000:
            return f"{self.name} надо провести полную диагностику."
        else:
            return f"{self.name} лучше не покупать."


"""Создание экземпляров класса и проверка методов"""

vehicle1 = Vehicle("Honda", 30000)
vehicle2 = Vehicle("Audi", 80000)
vehicle3 = Vehicle("Toyota", 120000)
vehicle4 = Vehicle("Renault", 160000)

print(vehicle1.get_vehicle_type(2))
print(vehicle1.get_vehicle_advice())

print(vehicle2.get_vehicle_type(4))
print(vehicle2.get_vehicle_advice())

print(vehicle3.get_vehicle_type(4))
print(vehicle3.get_vehicle_advice())

print(vehicle4.get_vehicle_type(4))
print(vehicle4.get_vehicle_advice())