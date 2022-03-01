import scipy.optimize as opt
import numpy as np


def cost(x):
    ret = 0
    for i in range(len(x)):
        ret += x[i] * f[i]
    return ret


def obracun(xtek):
    ax = np.matmul(A, xtek)
    if np.all(ax <= b):
        global maximum
        if cost(xtek) > maximum:
            maximum = cost(xtek)
            global x_final
            x_final = xtek


def rekurzija(depth):
    x_tek[depth] = x_fix[depth]
    global korekcija
    if var[depth] == 1:
        for i in korekcija:
            x_tek[depth] += i
            if x_tek[depth] < 0:
                continue
            if depth > 0:
                rekurzija(depth - 1)
            else:
                obracun(x_tek)
    else:
        if depth > 0:
            rekurzija(depth - 1)
        else:
            obracun(x_tek)


A = np.array([[1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
              [480, 650, 580, 390, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 480, 650, 580, 390, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 480, 650, 580, 390],
              [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
              [0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
              [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
              [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1]])
b = np.array([10, 16, 8, 6800, 8700, 4300, 18, 15, 23, 12])
f = np.array([310, 380, 350, 285, 310, 380, 350, 285, 310, 380, 350, 285])

res = opt.linprog(-f, A, b, method='interior-point')

x0 = np.round(res.x, 8)
x_fix = [0] * 12
x_tek = [0] * 12
x_final = [0] * 12
var = [0] * 12
for i in range(len(x0)):
    if (x0[i] - int(x0[i])) != 0:
        var[i] = 1
        x_tek[i] = x0[i]
    else:
        x_tek[i] = int(x0[i])
    x_fix[i] = int(x0[i])

print("Necelobrojna resenja su:")
print(x_tek)
print("Odgovarajuci maksimalni racunski kapacitet je {:.8f} \n".format((-1) * res.fun))

maximum = 0
global_depth = 11
korekcija = [0, -1, -1, 3, 1, 1]
# print(np.matmul(A, x), cost(res.x))
# print(x)

rekurzija(global_depth)

print("Celobrojna resenja su:")
print(x_final)
print("Odgovarajuci maksimalni racunski kapacitet je {} \n".format(maximum))
input('Press ENTER to exit')
