from random import randint

class Dice():
    """класс предстовляющий игральные кости с заданным числом граней, по умолчанию - 6"""
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        """Возвращает случайное число от 1 до кол-ва граней."""
        return randint(1,self.sides)
            
