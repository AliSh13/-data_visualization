from random import randint
from mimesis import Person

class RandomPlayer():
    """Создает случайного игрока с случайными характеристиками"""
    def __init__(self):
        self.characteristics = []
        self.person = Person('en')

    def create_player(self):
        """ Создает имя и возраст """
        name = self.person.full_name()
        return '{}'.format(name)

    def create_characteristics(self):
        """Создает список хар-ик"""
        self.characteristics = []
        for char in range(6):
            char = randint(30,99)
            self.characteristics.append(char)
        return self.characteristics
