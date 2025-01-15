import doctest
from abc import ABC, abstractmethod


class Table(ABC):
    def __init__(self, material: str, height: float, width: float):
        """
        Создание и подготовка к работе объекта "Стол".

        :param material: Материал стола (например, дерево, стекло).
        :param height: Высота стола в сантиметрах.
        :param width: Ширина стола в сантиметрах.

        Примеры:
        >>> table = DiningTable("дерево", 75.0, 120.0)
        """
        if not isinstance(material, str):
            raise TypeError("Материал должен быть строкой.")
        if not isinstance(height, (int, float)) or height <= 0:
            raise ValueError("Высота должна быть положительным числом.")
        if not isinstance(width, (int, float)) or width <= 0:
            raise ValueError("Ширина должна быть положительным числом.")

        self.material = material
        self.height = height
        self.width = width

    @abstractmethod
    def adjust_height(self, new_height: float) -> None:
        """
        Регулировка высоты стола.

        :param new_height: Новая высота стола.
        :raise ValueError: Если новая высота некорректна.

        Примеры:
        >>> table = DiningTable("дерево", 75.0, 120.0)
        >>> table.adjust_height(80.0)
        """
        ...

    @abstractmethod
    def fold_table(self) -> None:
        """
        Складной стол: выполнить складывание.
        """
        ...


class DiningTable(Table):
    def adjust_height(self, new_height: float) -> None:
        if new_height <= 0:
            raise ValueError("Высота должна быть положительным числом.")
        self.height = new_height

    def fold_table(self) -> None:
        pass


class Tree(ABC):
    def __init__(self, species: str, age: int, height: float):
        """
        Создание и подготовка объекта "Дерево".

        :param species: Вид дерева (например, дуб, сосна).
        :param age: Возраст дерева в годах.
        :param height: Высота дерева в метрах.

        Примеры:
        >>> tree = OakTree("дуб", 10, 5.5)
        """
        if not isinstance(species, str):
            raise TypeError("Вид дерева должен быть строкой.")
        if not isinstance(age, int) or age < 0:
            raise ValueError("Возраст должен быть целым неотрицательным числом.")
        if not isinstance(height, (int, float)) or height <= 0:
            raise ValueError("Высота должна быть положительным числом.")

        self.species = species
        self.age = age
        self.height = height

    @abstractmethod
    def grow(self, years: int) -> None:
        """
        Увеличение возраста и высоты дерева.

        :param years: Количество лет, в течение которых дерево растет.
        :raise ValueError: Если количество лет меньше или равно нулю.

        Примеры:
        >>> tree = OakTree("дуб", 10, 5.5)
        >>> tree.grow(5)
        """
        ...

    @abstractmethod
    def shed_leaves(self) -> None:
        """
        Выполнение процесса опадания листьев.
        """
        ...


class OakTree(Tree):
    def grow(self, years: int) -> None:
        if years <= 0:
            raise ValueError("Количество лет должно быть положительным числом.")
        self.age += years
        self.height += years * 0.5

    def shed_leaves(self) -> None:
        pass


class SocialNetwork(ABC):
    def __init__(self, name: str, user_count: int):
        """
        Создание и подготовка объекта "Социальная сеть".

        :param name: Название социальной сети.
        :param user_count: Количество пользователей.

        Примеры:
        >>> network = Facebook("Facebook", 3000000)
        """
        if not isinstance(name, str):
            raise TypeError("Название должно быть строкой.")
        if not isinstance(user_count, int) or user_count < 0:
            raise ValueError("Количество пользователей должно быть неотрицательным целым числом.")

        self.name = name
        self.user_count = user_count

    @abstractmethod
    def add_user(self, username: str) -> None:
        """
        Добавление нового пользователя в социальную сеть.

        :param username: Имя пользователя.
        :raise ValueError: Если имя пользователя некорректно.

        Примеры:
        >>> network = Facebook("Facebook", 3000000)
        >>> network.add_user("JohnDoe")
        """
        ...

    @abstractmethod
    def remove_user(self, username: str) -> None:
        """
        Удаление пользователя из социальной сети.

        :param username: Имя пользователя.
        :raise ValueError: Если пользователя с таким именем не существует.

        Примеры:
        >>> network = Facebook("Facebook", 3000000)
        >>> network.remove_user("JohnDoe")
        """
        ...


class Facebook(SocialNetwork):
    def add_user(self, username: str) -> None:
        if not isinstance(username, str) or not username.strip():
            raise ValueError("Имя пользователя должно быть непустой строкой.")
        self.user_count += 1

    def remove_user(self, username: str) -> None:
        if not isinstance(username, str) or not username.strip():
            raise ValueError("Имя пользователя должно быть непустой строкой.")
        self.user_count -= 1


if __name__ == "__main__":
    doctest.testmod()
