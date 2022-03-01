import numpy as np
import random
import math

N = 20
R0 = 15
F = 0.8
CR = 0.9
population = 60
gen = 10**4
D = 6
tacnost = 10**(-14)
S = (2.424595205726587e-01, 1.737226395065819e-01, 1.315612759386036e-01,
     1.022985539042393e-01, 7.905975891960761e-02, 5.717509542148174e-02,
     3.155886625106896e-02, -6.242228581847679e-03, -6.565183775481365e-02,
     -8.482380513926287e-02, -1.828677714588237e-02, 3.632382803076845e-02,
     7.654845872485493e-02, 1.152250132891757e-01, 1.631742367154961e-01,
     2.358469152696193e-01, 3.650430801728451e-01, 5.816044173713664e-01,
     5.827732223753571e-01, 3.686942505423780e-01)


def cost(x):
    x1 = x[0]
    y1 = x[1]
    x2 = x[2]
    y2 = x[3]
    a1 = x[4]
    a2 = x[5]
    if math.sqrt(x1 ** 2 + y1 ** 2) < R0 and math.sqrt(x2 ** 2 + y2 ** 2) < R0:
        y = 0
        for i in range(N):
            y += (a1 / math.sqrt((xi[i] - x1) ** 2 + (yi[i] - y1) ** 2) + a2 / math.sqrt(
                (xi[i] - x2) ** 2 + (yi[i] - y2) ** 2) - S[i]) ** 2
        return y
    else:
        return 100


def selekcija(p, a, b, c):
    z = niz[a] + F * np.subtract(niz[b], niz[c])
    R = random.randint(0, D - 1)
    niz_tek = [0] * 6
    for i in range(D):
        ri = random.uniform(0, 1)
        if ri < CR or i == R:
            niz_tek[i] = z[i]
        else:
            niz_tek[i] = niz[p][i]
    if cost(niz_tek) < cost(niz[p]):
        niz[p] = niz_tek.copy()


xi = [0] * 20
yi = [0] * 20
for i in range(N):
    xi[i] = R0 * math.cos(2 * math.pi * i / N)
    yi[i] = R0 * math.sin(2 * math.pi * i / N)

xmin = [0] * 6
fmin = 100

niz = [0] * population
for i in range(population):
    x1 = random.uniform(-15, 15)
    y1 = random.uniform(-15, 15)
    x2 = random.uniform(-15, 15)
    y2 = random.uniform(-15, 15)
    a1 = random.uniform(-15, 15)
    a2 = random.uniform(-15, 15)
    niz[i] = np.array([x1, y1, x2, y2, a1, a2])

for g in range(gen):
    for i in range(population):
        f = cost(niz[i])
        if f < fmin:
            fmin = f
            xmin = niz[i].copy()
    if fmin < tacnost:
        break
    for p in range(population):
        while True:
            a = random.randint(0, population - 1)
            if a != p:
                break
        while True:
            b = random.randint(0, population - 1)
            if b != p and b != a:
                break
        while True:
            c = random.randint(0, population - 1)
            if c != p and c != a and c != b:
                break
        selekcija(p, a, b, c)

print("Minimum optimizacione f-je je {}\nA tacke su {}".format(fmin, xmin))
input('Press ENTER to exit')
