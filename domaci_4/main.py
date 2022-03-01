import matplotlib.pyplot as plt
import numpy as np
import scipy.special as scipy


def prepolovi(a, b, i):
    while b - a > e:
        t = (a + b) / 2
        if scipy.spherical_jn(i, a, False) * scipy.spherical_jn(i, t, False) < 0:
            b = t
        else:
            a = t
    return t


# main funkcija
e = 10 ** (-12)
t1 = prepolovi(4, 6, 1)
t2 = prepolovi(6, 8, 1)
t3 = prepolovi(5, 7, 2)
t4 = prepolovi(8, 10, 2)

print("Prva nula sferne Beselove funkcije J1 je %.12f" % round(t1, 12))
print("Druga nula sferne Beselove funkcije J1 je {:.12f}".format(t2))
print("Prva nula sferne Beselove funkcije J2 je {:.12f}".format(t3))
print("Druga nula sferne Beselove funkcije J2 je {:.12f}".format(t4))

fig = plt.figure()
x = np.arange(0, 20, 0.5)
plt.xticks(np.arange(0, 21, step=2))
plt.plot(x, scipy.spherical_jn(1, x, False), label='j1')
plt.plot(x, scipy.spherical_jn(2, x, False), label='j2')
plt.legend()
plt.show()
