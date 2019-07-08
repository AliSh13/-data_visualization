from random import choice

class RandomWalk():
    """Генерация случайного блуждения"""
    def __init__(self, num_points = 5000):
        self.num_points = num_points
        # задаем начальную точку (0,0)
        self.x_values = [0]
        self.y_values = [0]

    def generation_step(self):
        """Определяет направление и длину шага """
        direction = choice([1,-1])
        distance = choice([0,1,2,3,4])
        step = direction * distance

        return step

    def fill_walk(self):
        """Вычисляет все точки блуждения"""
        while len(self.x_values) < self.num_points:

            #вычисление следующих значений
            next_x = self.x_values[-1] + self.generation_step()
            next_y = self.y_values[-1] + self.generation_step()

            # отклонение нулевых перемещений
            if next_x == self.x_values[-1] and next_y == self.y_values[-1]:
                continue

            self.x_values.append(next_x)
            self.y_values.append(next_y)
