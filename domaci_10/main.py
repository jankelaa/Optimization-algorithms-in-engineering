import numpy as np
import random
import math

w = 0.729
c1 = c2 = 1.494
vmax = 1.4
swarm = 60
maxiter = 10 ** 6
xsize = 6
espilon = 10 ** (-14)

a = [1, 5, 1]
b = [3, 2, 0]
c = [5, 7, 1]
d = [6, 3, 3]


def cost(x):
    return math.sqrt((x[0] - a[0]) ** 2 + (x[1] - a[1]) ** 2 + (x[2] - a[2]) ** 2) + \
           math.sqrt((x[0] - b[0]) ** 2 + (x[1] - b[1]) ** 2 + (x[2] - b[2]) ** 2) + \
           math.sqrt((x[3] - c[0]) ** 2 + (x[4] - c[1]) ** 2 + (x[5] - c[2]) ** 2) + \
           math.sqrt((x[3] - d[0]) ** 2 + (x[4] - d[1]) ** 2 + (x[5] - d[2]) ** 2) + \
           math.sqrt((x[0] - x[3]) ** 2 + (x[1] - x[4]) ** 2 + (x[2] - x[5]) ** 2)


def optimize(index):
    v[index] = w * v[index] + \
               c1 * random.uniform(0, 1) * (pbest[index] - x[index]) + \
               c2 * random.uniform(0, 1) * (gbest - x[index])
    for i in range(xsize - 1):
        if v[index][i] > vmax:
            v[index][i] = vmax
        if v[index][i] < -1 * vmax:
            v[index][i] = -1 * vmax
    x[index] = x[index] + v[index]


gbest = [0] * 6
dbest = 100
x = [0] * swarm
v = [0] * swarm
pbest = [0] * swarm
dpbest = [100000] * swarm
for i in range(swarm):
    x1 = random.uniform(0, 7)
    y1 = random.uniform(0, 7)
    z1 = random.uniform(0, 7)
    x2 = random.uniform(0, 7)
    y2 = random.uniform(0, 7)
    z2 = random.uniform(0, 7)
    x[i] = np.array([x1, y1, z1, x2, y2, z2])
    v[i] = np.array([0, 0, 0, 0, 0, 0])

while True:
    cnt = 0
    for j in range(swarm):
        if cost(x[j]) < dpbest[j]:
            dpbest[j] = cost(x[j])
            pbest[j] = x[j].copy()
            if dpbest[j] < dbest:
                dbest = dpbest[j]
                gbest = pbest[j].copy()
        optimize(j)
    for j in range(swarm):
        if abs(dpbest[j] - dbest) < espilon:
            cnt = cnt + 1
    if cnt == 60:
        break
print("Minimum optimizacione f-je je {}\nS1({}, {}, {})\nS2({}, {}, {})".format(dbest, gbest[0], gbest[1], gbest[2],
                                                                              gbest[3], gbest[4], gbest[5]))
input('Press ENTER to exit')
