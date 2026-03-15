class Vehicle:
    """
    Базовый класс для транспортных средств.
    """
    def __init__(self, brand: str, model: str, year: int, max_speed: int):
        """
        Конструктор базового класса Vehicle.
        :param brand: марка транспортного средства
        :param model: модель транспортного средства
        :param year: год выпуска
        :param max_speed: максимальная скорость
        """
        self.brand = brand
        self.model = model
        self.year = year
        self.max_speed = max_speed
        self._is_running = False  # Непубличный атрибут — состояние двигателя (работает/нет)

    def __str__(self) -> str:
        """Возвращает строковое представление объекта."""
        return f"{self.brand} {self.model} ({self.year}) max speed: {self.max_speed} km/h"

    def __repr__(self) -> str:
        """Возвращает официальное строковое представление объекта для отладки."""
        return f"Vehicle(brand='{self.brand}', model='{self.model}', year={self.year}, max_speed={self.max_speed})"

    def start_engine(self) -> None:
        """Запускает двигатель транспортного средства."""
        self._is_running = True
        print(f"Двигатель {self.brand} {self.model} запущен.")

    def stop_engine(self) -> None:
        """Останавливает двигатель транспортного средства."""
        self._is_running = False
        print(f"Двигатель {self.brand} {self.model} остановлен.")


class Car(Vehicle):
    """
    Дочерний класс для легковых автомобилей.
    Унаследует атрибуты и методы от класса Vehicle, расширяет их с учётом специфики легковых авто.
    """
    def __init__(self, brand: str, model: str, year: int, max_speed: int, trunk_volume: float):
        """
        Расширяет конструктор базового класса, добавляя атрибут trunk_volume (объём багажника).
        :param brand: марка автомобиля
        :param model: модель автомобиля
        :param year: год выпуска
        :param max_speed: максимальная скорость
        :param trunk_volume: объём багажника в литрах
        """
        super().__init__(brand, model, year, max_speed)
        self.trunk_volume = trunk_volume

    def __str__(self) -> str:
        """Переопределяет метод __str__ для добавления информации об объёме багажника."""
        return f"{super().__str__()} trunk volume: {self.trunk_volume} L"

    def __repr__(self) -> str:
        """Переопределяет метод __repr__ для добавления информации об объёме багажника."""
        return f"Car(brand='{self.brand}', model='{self.model}', year={self.year}, " \
               f"max_speed={self.max_speed}, trunk_volume={self.trunk_volume})"

    def start_engine(self) -> None:
        """Перегружает метод start_engine для добавления проверки на наличие топлива.
        Причина перегрузки: для легковых автомобилей важно учитывать уровень топлива перед запуском двигателя."""
        if self._check_fuel_level():
            super().start_engine()
        else:
            print("Недостаточно топлива для запуска двигателя.")

    def _check_fuel_level(self) -> bool:
        """Непубличный метод для проверки уровня топлива.
        В реальной реализации здесь бы был код для проверки датчика уровня топлива.
        :return: True, если топлива достаточно, False — иначе
        """
        # Имитация проверки уровня топлива
        return True

    def open_trunk(self) -> None:
        """Метод для открытия багажника.
        Специфичен для легковых автомобилей."""
        print(f"Багажник автомобиля {self.brand} {self.model} открыт.")


class Truck(Vehicle):
    """
    Дочерний класс для грузовых автомобилей.
    Унаследует атрибуты и методы от класса Vehicle, расширяет их с учётом специфики грузовых авто.
    """
    def __init__(self, brand: str, model: str, year: int, max_speed: int, cargo_capacity: float):
        """
        Расширяет конструктор базового класса, добавляя атрибут cargo_capacity (грузоподъёмность).
        :param brand: марка грузовика
        :param model: модель грузовика
        :param year: год выпуска
        :param max_speed: максимальная скорость
        :param cargo_capacity: грузоподъёмность в тоннах
        """
        super().__init__(brand, model, year, max_speed)
        self.cargo_capacity = cargo_capacity
        self._cargo_weight = 0  # Непубличный атрибут — текущий вес груза

    def __str__(self) -> str:
        """Переопределяет метод __str__ для добавления информации о грузоподъёмности."""
        return f"{super().__str__()} cargo capacity: {self.cargo_capacity} t, current cargo weight: {self._cargo_weight} t"

    def __repr__(self) -> str:
        """Переопределяет метод __repr__ для добавления информации о грузоподъёмности."""
        return f"Truck(brand='{self.brand}', model='{self.model}', year={self.year}, " \
               f"max_speed={self.max_speed}, cargo_capacity={self.cargo_capacity})"

    def load_cargo(self, weight: float) -> None:
        """
        Метод для загрузки груза.
        Перегружает логику работы с весом груза, проверяет, не превышает ли он грузоподъёмность.
        :param weight: вес груза для загрузки
        """
        if weight > self.cargo_capacity:
            print(f"Ошибка: вес груза ({weight} т) превышает грузоподъёмность ({self.cargo_capacity} т).")
        else:
            self._cargo_weight += weight
            print(f"Груз весом {weight} т загружен. Текущий вес груза: {self._cargo_weight} т.")

    def unload_cargo(self, weight: float) -> None:
        """Метод для разгрузки груза."""
        if weight > self._cargo_weight:
            print(f"Ошибка: нельзя разгрузить {weight} т, текущий вес груза — {self._cargo_weight} т.")
        else:
            self._cargo_weight -= weight
            print(f"Разгружено {weight} т. Текущий вес груза: {self._cargo_weight} т.")


if __name__ == "__main__":
    # Создаём экземпляры классов
    car = Car("Toyota", "Camry", 2020, 220, 500)
    truck = Truck("KamAZ", "5490", 2019, 110, 15)

    # Демонстрируем работу методов
    print(car)  # Используем __str__
    print(repr(car))  # Используем __repr__
    car.start_engine()  # Запуск двигателя с проверкой топлива
    car.open_trunk()  # Специфический метод для легковых авто

    print("\n" + "-" * 50 + "\n")

    print(truck)  # Используем __str__
    print(repr(truck))  # Используем __repr__
    truck.start_engine()  # Запуск двигателя (унаследован от базового класса)
    truck.load_cargo(10)  # Загрузка груза
    truck.unload_cargo(5)  # Разгрузка груза
