import numpy as np
import random
import matplotlib.pyplot as plt

skup = 10000


def opt_prva(x1, x2):
    return 2*x1**2 + x2**2


def opt_druga(x1, x2):
    return -1*(x1-x2)**2


f1 = [0] * skup
f2 = [0] * skup
for i in range(skup):
    x1 = random.uniform(-1, 1)
    x2 = random.uniform(-1, 1)
    f1[i] = opt_prva(x1, x2)
    f2[i] = opt_druga(x1, x2)

pareto_front = []
for i in range(skup):
    cnt = 0
    for j in range(skup):
        cnt += 1
        if i == j:
            continue
        if f1[j] <= f1[i]:
            if f2[j] < f2[i]:
                break
    if cnt == skup:
        pareto_front.append((f1[i], f2[i]))

plt.figure("Pareto front bez dodatnog uslova")
for i in range(skup):
    plt.plot(f1[i], f2[i], '.', color='blue')
for i in range(len(pareto_front)):
    plt.plot(pareto_front[i][0], pareto_front[i][1], '.', color='red')
plt.xlabel('f1')
plt.ylabel('f2')
plt.grid()
plt.show()

#
# sada sve isto
# samo uz dodatni uslov
#
pareto_front.clear()
for i in range(skup):
    while True:
        x1 = random.uniform(-1, 1)
        x2 = random.uniform(-1, 1)
        if (x1*x2 + 1/4) >= 0:
            break
    f1[i] = opt_prva(x1, x2)
    f2[i] = opt_druga(x1, x2)

for i in range(skup):
    cnt = 0
    for j in range(skup):
        cnt += 1
        if i == j:
            continue
        if f1[j] <= f1[i]:
            if f2[j] < f2[i]:
                break
    if cnt == skup:
        pareto_front.append((f1[i], f2[i]))

plt.figure("Pareto front sa dodatnim uslovom")
for i in range(skup):
    plt.plot(f1[i], f2[i], '.', color='blue')
for i in range(len(pareto_front)):
    plt.plot(pareto_front[i][0], pareto_front[i][1], '.', color='red')
plt.xlabel('f1')
plt.ylabel('f2')
plt.grid()
plt.show()
