from abc import ABC, abstractmethod


class Transport(ABC):
    # Статическое поле для подсчета общего количества транспортных средств
    total_transport_count = 0

    def __init__(self, brand: str, model: str):
        self.__brand = brand  # Скрытое поле
        self.__model = model  # Скрытое поле
        Transport.total_transport_count += 1

    @abstractmethod
    def get_info(self):
        pass

    @classmethod
    def get_total_transport_count(cls):
        return cls.total_transport_count

    def display_brand(self):
        return f"Brand: {self.__brand}"


class Car(Transport):
    def __init__(self, brand: str, model: str, fuel_type: str, doors: int):
        super().__init__(brand, model)
        self.fuel_type = fuel_type  # Открытое поле
        self.doors = doors  # Открытое поле

    def get_info(self):
        return f"Car: {self.display_brand()}, Model: {self._Transport__model}, Fuel Type: {self.fuel_type}, Doors: {self.doors}"

    def calculate_fuel_efficiency(self, distance: float, fuel_consumed: float):
        if fuel_consumed == 0:
            return "Fuel consumed cannot be zero."
        return distance / fuel_consumed


class Bicycle(Transport):
    def __init__(self, brand: str, model: str, gear_count: int, has_basket: bool):
        super().__init__(brand, model)
        self.gear_count = gear_count  # Открытое поле
        self.has_basket = has_basket  # Открытое поле

    def get_info(self):
        return f"Bicycle: {self.display_brand()}, Model: {self._Transport__model}, Gear Count: {self.gear_count}, Has Basket: {self.has_basket}"

    def calculate_trip_time(self, distance: float, speed: float):
        if speed == 0:
            return "Speed cannot be zero."
        return distance / speed


# Пример использования классов
if __name__ == "__main__":
    car1 = Car("Toyota", "Corolla", "Petrol", 4)
    bicycle1 = Bicycle("Giant", "Escape 3", 21, True)

    print(car1.get_info())
    print(f"Fuel Efficiency: {car1.calculate_fuel_efficiency(100, 5)} km/l")

    print(bicycle1.get_info())
    print(f"Trip Time: {bicycle1.calculate_trip_time(10, 15)} hours")

    print(f"Total Transport Count: {Transport.get_total_transport_count()}")
