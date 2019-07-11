"""Моделирование броска игральных костей и сравнение броска 1 кубика
, двух кубиков и двух кубиков разных размеров"""

import pygal
from dice import Dice

#создание кубика и имитация заданного числа бросков
dice = Dice()
dice_roll1 = [dice.roll() for _ in range(1000)]
#анализ результатов
result1 = [dice_roll1.count(value) for value in range(1,dice.sides + 1)]

#моделирование бросков 2 кубиков
dice1 = Dice()
dice_roll2 = [dice1.roll() + dice1.roll() for _ in range(1000)]
#анализ результатов
result2 = [dice_roll2.count(value) for value in range(1,max(dice_roll2) + 1)]

#моделирование бросков 2 кубиков разных размеров
dice3 = Dice()
dice4 = Dice(10)
dice_roll3 = [dice3.roll() + dice4.roll() for _ in range(1000)]
#анализ результатов
result3 = [dice_roll3.count(value) for value in range(1,max(dice_roll3) + 1)]


hist = pygal.Bar()
hist.title = 'Анализ бросков кубика'
hist.x_labels = [_ for _ in range(1,max(dice_roll3) + 1)]
hist.x_title = 'Брсоок'
hist.y_title = 'Результат бросков'
hist.add('D6', result1)
hist.add('D6 + D6', result2)
hist.add('D6 + D10', result3)
hist.render_to_file('Roll dice/dice_visual.svg')
