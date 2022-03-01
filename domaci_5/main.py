import numpy as np
import scipy.optimize as opt
import matplotlib.pyplot as plt


# izlaz mreze na osnovu ulaza
def yout(w, xin):
    y = 0.0
    for k in range(n):
        y += w[k + 5] * a(w[k] * xin)
    return a(y)


# aktivaciona f-ja
def a(y):
    return np.tanh(y)


# ytraining
def ytraining(xin):
    return 0.5 * np.sin(np.pi * xin)


# optimizaciona f-ja
def optimize(w):
    xin = -1
    f = 0.0
    for wi in w:
        if wi < -10 or wi > 10:
            return 1e14
    while xin < 1:
        f += (yout(w, xin) - ytraining(xin)) ** 2
        xin += 0.1
    return np.sqrt(f)


# main
n = 5
w0 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
w1 = [1, 2, 3, 4, 5, -3, -4, -5, 0, 2.5]
print("a) Izlaz yout za sve koeficijente w0=[1]*10 je " + str(yout(w0, 1)))
print("b) Optimizaciona f-ja za sve koeficijente w0=[1]*10 je " + str(optimize(w0)))
# result = opt.minimize(optimize, w0, method='Nelder-Mead', options={'maxfev': 1e14})
while True:
    result = opt.minimize(optimize, w1, method='Nelder-Mead', options={'maxfev': 1e14})
    if result.fun < 1e-2:
        break
# print(result)
print("c) Vrednost minimalne pronadjene optimizacione funkcije za ulaze")
print("w = {} je {}".format(w1, result.fun))
print("Dobijeni koeficijenti su:")
for i in range(10):
    #    print(result.x[i])
    print("w[{}] = ".format(i + 1) + "{:.15f}".format(result.x[i]))

fig = plt.figure()
x = np.arange(-1.0, 1.1, 0.1)
plt.xticks(np.arange(-1.0, 1.2, step=0.2))
plt.plot(x, ytraining(x), label='ytraining')
plt.plot(x, yout(result.x, x), label='yout')
plt.legend()
plt.grid()
plt.show()
