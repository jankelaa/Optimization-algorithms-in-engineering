import numpy as np
import random
import math
import matplotlib.pyplot as plt

max_iter = 100000
D = 64
h_max = 32
h_min = 1
M = 20
f_max = 2 ** 26
t0 = 32 * 1024 * 1024
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


def prihvati(e1, e0):
    if e1 < e0:
        return True
    else:
        p = math.exp(-1 * (e1 - e0) / t)
        if random.uniform(0, 1) <= p:
            return True
        else:
            return False


def sat_hamming(x):
    h = int((h_min - h_max) * (i - 1) / (max_iter - 1) + h_max)
    y = random.sample(range(0, 64), h)
    for k in y:
        if x[k] == 1:
            x[k] = 0
        else:
            x[k] = 1
    return x


def temp():
    return 0.95 * t


c = [0] * M
f_konacno = f_max
x_konacno = [0] * D

for k in range(M):
    x_min = x = np.random.randint(2, size=64)
    f_min = f0 = cost(x)
    c[k] = [f0]
    t = t0
    # print(f_max - np.matmul(x, s))

    for i in range(max_iter):
        x_tek = sat_hamming(x)
        f1 = cost(x_tek)
        if prihvati(f1, f0):
            x = x_tek
            f0 = f1
            if f1 < f_min:
                x_min = x
                f_min = f1
                if f_min == 0:
                    break
        t = temp()
        c[k].append(f_min)

    if f_min < f_konacno:
        f_konacno = f_min
        x_konacno = x_min
    # print(f_max - np.matmul(x_min, s))
    print("Minimalna f-ja {}. ponavljanja je {} \nA tacke su {}".format(k, f_min, x_min))

print("Konacna minimalna f-ja nakon 20 ponavljanja je {} \nA tacke su {}".format(f_konacno, x_konacno))

plt.figure("Kumulativni minimum")
plt.yscale("log")
plt.xscale("log")
for i in range(M):
    plt.plot(c[i], label="C{}".format(i))
plt.legend()
plt.grid()
plt.show()

csr = []
for i in range(max_iter):
    cik = 0
    for j in c:
        cik += j[i]
    csr.append(cik / M)
plt.figure("Srednje resenje")
plt.yscale("log")
plt.xscale("log")
plt.plot(csr, label="C_SREDNJE")
plt.legend()
plt.grid()
plt.show()
