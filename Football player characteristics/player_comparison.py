import pygal
from Players import RandomPlayer

radar_chart = pygal.Radar(legend_at_bottom=True)
radar_chart.title = 'Сравнение игроков футбола'
radar_chart.x_labels = ['Сила', 'Скорость', 'Дриблинг', 'Удар', 'Атака', 'Защита']
#генерирует заданное число игроков
for player in range(6):
    radar_chart.add(RandomPlayer().create_player(),
                    RandomPlayer().create_characteristics())

radar_chart.render_to_file('Football player characteristics/visual_player_comparison.svg')
