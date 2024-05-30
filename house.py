class House:
    def __init__(self, location, color, size, price):
        self.location = location
        self.color = color
        self.size = size
        self.price = price

    def display_info(self):
        print(f"Дом находится {self.location} цвет {self.color} площадь {self.size}")

    def calculate_discounted_price(self, discount):
        discounted_price = self.price * (1 - discount)
        return discounted_price

# Создание экземпляров класса House
house1 = House("у озера", "серый", "150", 2000000)
house2 = House("возле леса", "белый", "200", 3000000)

# Вызов методов экземпляров
house1.display_info()
discounted_price = house1.calculate_discounted_price(0.1)
print(f"Цена дома 1 со скидкой: {discounted_price}")
house2.display_info()
discounted_price = house2.calculate_discounted_price(0.1)
print(f"Цена дома 2 со скидкой: {discounted_price}")