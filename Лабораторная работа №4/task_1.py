from typing import Any

class Animal:
    """
    Базовый класс Animal, представляющий общее понятие животного.
    Атрибуты:
        name (str): Имя животного.
        habitat (str): Среда обитания.
    Методы:
        move() -> str: Возвращает строку, описывающую, как животное передвигается.
    """

    def __init__(self, name: str, habitat: str) -> None:
        self.name = name
        self.habitat = habitat

    def __str__(self) -> str:
        return f"Animal(name={self.name}, habitat={self.habitat})"

    def __repr__(self) -> str:
        return f"<Animal name={self.name} habitat={self.habitat}>"

    def move(self) -> str:
        return f"{self.name} moves in its environment."


class Mammal(Animal):
    """
    Дочерний класс Mammal, представляющий млекопитающих.
    Наследует атрибуты и методы класса Animal и добавляет новые.
    Атрибуты:
        has_fur (bool): Наличие шерсти.
    Методы:
        feed_milk() -> str: Возвращает строку, описывающую процесс кормления молоком.
    """

    def __init__(self, name: str, habitat: str, has_fur: bool) -> None:
        # Расширяем конструктор базового класса, добавляя новый атрибут.
        super().__init__(name, habitat)
        self.has_fur = has_fur

    def __str__(self) -> str:
        return f"Mammal(name={self.name}, habitat={self.habitat}, has_fur={self.has_fur})"

    def __repr__(self) -> str:
        return f"<Mammal name={self.name} habitat={self.habitat} has_fur={self.has_fur}>"

    def feed_milk(self) -> str:
        """
        Описание процесса кормления молоком, характерного для млекопитающих.
        """
        return f"{self.name} feeds its young with milk."

    def move(self) -> str:
        """
        Переопределение метода move().
        Причина: для млекопитающих необходимо уточнить, что большинство из них ходит или бегает.
        """
        return f"{self.name} walks or runs."


class Bird(Animal):
    """
    Дочерний класс Bird, представляющий птиц.
    Наследует атрибуты и методы класса Animal и добавляет новые.
    Атрибуты:
        can_fly (bool): Умеет ли птица летать.
    Методы:
        lay_eggs() -> str: Возвращает строку, описывающую процесс откладывания яиц.
    """

    def __init__(self, name: str, habitat: str, can_fly: bool) -> None:
        # Расширяем конструктор базового класса, добавляя новый атрибут.
        super().__init__(name, habitat)
        self.can_fly = can_fly

    def __str__(self) -> str:
        return f"Bird(name={self.name}, habitat={self.habitat}, can_fly={self.can_fly})"

    def __repr__(self) -> str:
        return f"<Bird name={self.name} habitat={self.habitat} can_fly={self.can_fly}>"

    def lay_eggs(self) -> str:
        """
        Описание процесса откладывания яиц, характерного для птиц.
        """
        return f"{self.name} lays eggs."

    def move(self) -> str:
        """
        Переопределение метода move().
        Причина: для птиц необходимо уточнить, что большинство из них летает.
        """
        return f"{self.name} flies through the air." if self.can_fly else f"{self.name} walks or hops."

# Пример использования классов
if __name__ == "__main__":
    mammal = Mammal(name="Lion", habitat="Savannah", has_fur=True)
    bird = Bird(name="Penguin", habitat="Antarctica", can_fly=False)

    print(mammal)
    print(mammal.move())
    print(mammal.feed_milk())

    print(bird)
    print(bird.move())
    print(bird.lay_eggs())
