import numpy as np
import random
import matplotlib.pyplot as plt
from operator import attrgetter
from collections import namedtuple
import copy

population = 2000
gen = 50
D = 64
M = 20
f_max = 2 ** 26
s = [173669, 275487, 1197613, 1549805, 502334, 217684, 1796841, 274708,
     631252, 148665, 150254, 4784408, 344759, 440109, 4198037, 329673, 28602,
     144173, 1461469, 187895, 369313, 959307, 1482335, 2772513, 1313997, 254845,
     486167, 2667146, 264004, 297223, 94694, 1757457, 576203, 8577828, 498382,
     8478177, 123575, 4062389, 3001419, 196884, 617991, 421056, 3017627, 131936,
     1152730, 2676649, 656678, 4519834, 201919, 56080, 2142553, 326263, 8172117,
     2304253, 4761871, 205387, 6148422, 414559, 2893305, 2158562, 465972, 304078,
     1841018, 1915571]


def cost(x):
    f_tek = np.matmul(x, s)
    if f_tek <= f_max:
        return f_max - f_tek
    else:
        return f_max


def mutacija(x):
    bit = random.randint(0, D - 1)
    if x[bit] == 1:
        x[bit] = 0
    else:
        x[bit] = 1
    return x


def ukrstanje(p1, p2):
    cut = random.randint(1, D - 1)
    tek_x = p2.x.copy()
    for i in range(cut):
        tek_x[i] = p1.x[i]
    if random.uniform(0, 1) <= 0.1:
        tek_x = mutacija(tek_x)
    return tek_x


def selekcija():
    i = 0
    cnt = int(len(lista_old) / 5)
    if cnt % 2 == 1:
        cnt = cnt + 1
    del lista_old[cnt:]
    while True:
        lista_tek = copy.deepcopy(lista_old)
        random.shuffle(lista_tek)
        while lista_tek:
            parent1 = lista_tek.pop()
            parent2 = lista_tek.pop()
            if random.uniform(0, 1) <= 0.8:
                res = ukrstanje(parent1, parent2)
                lista_new.append(Struct(x=res, f=cost(res)))
                res = ukrstanje(parent2, parent1)
                lista_new.append(Struct(x=res, f=cost(res)))
                i = i + 2
            if i >= population:
                break
        if i >= population:
            break


# inicilalizacija
c = [0] * M
f_konacno = f_max
x_konacno = [0] * D
Struct = namedtuple('Struct', ['x', 'f'])
lista_old = []

for m in range(M):
    lista_new = []
    f_min = f_max
    x_min = [0] * D

    # generisanje pocetne populacije
    for i in range(population):
        x0 = np.random.randint(2, size=64)
        f0 = cost(x0)
        lista_new.append(Struct(x=x0, f=f0))
    c[m] = [f_min]
    for i in range(gen):
        lista_old = copy.deepcopy(lista_new)
        for lst in lista_old:
            if lst.f < f_min:
                c[m].append(lst.f)
                f_min = lst.f.copy()
                x_min = lst.x.copy()
            else:
                c[m].append(f_min)
        if f_min == 0:
            break
        lista_old.sort(key=attrgetter('f'))
        lista_new = []
        selekcija()
        lista_old = []

    # provere na kraju jednog ponavljanja
    if f_min < f_konacno:
        f_konacno = f_min
        x_konacno = x_min
    print("Minimalna f-ja {}. ponavljanja je {} \nA tacke su {}".format(m+1, f_min, list(x_min)))

print("\nKonacna minimalna f-ja nakon 20 ponavljanja je {} \nA tacke su {}".format(f_konacno, list(x_konacno)))

plt.figure("Kumulativni minimum")
plt.yscale("log")
plt.xscale("log")
for m in range(M):
    plt.plot(c[m], label="C{}".format(m))
plt.grid()
plt.show()

csr = []
for i in range(gen * population):
    cik = 0
    for j in c:
        if i >= len(j):
            cik += 0
        else:
            cik += j[i]
    csr.append(cik / M)
plt.figure("Srednje resenje")
plt.yscale("log")
plt.xscale("log")
plt.plot(csr, label="C_SREDNJE")
plt.grid()
plt.show()
