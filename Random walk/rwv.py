"""Visualization of random walk"""

import matplotlib.pyplot as plt

from RandomWalkGen import RandomWalk


rw = RandomWalk(15000)
rw.fill_walk()

point_numbers = list(range(rw.num_points))
plt.figure(figsize=(10, 6))
plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
            edgecolors='None', s=15)
plt.scatter(0, 0, c='red', s=50)
plt.scatter(rw.x_values[-1], rw.y_values[-1],c='green', s=50)
plt.title('Random walk')
#удаление осей
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)

plt.show()
