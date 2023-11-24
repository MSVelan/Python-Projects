import numpy as np
from matplotlib import pyplot as plt
import matplotlib.ticker as tick
from math import sin
pi = np.pi
t = np.arange(-4*pi,4*pi,0.01)

#Rectangular signal
xt1 = [1 if ((i>=-pi/2 and i<=pi/2) or (i>=-5*pi/2 and i<=-3*pi/2) or (i>=3*pi/2 and i<=5*pi/2) or (i>=-9*pi/2 and i<=-7*pi/2) or (i>=7*pi/2 and i<=9*pi/2)) else 0 for i in t]

#Approximated rectangular signal
xt2 = 1/2
#n = 20
#n= 100
#n = 200
n = 2000

for i in range(n):
    if(i%2!=0):
        xt2 += (2*np.sin(i*pi/2)/(i*pi))*(np.sin(i*t+pi/2))

fig, ax = plt.subplots()

plt.plot(t,xt2,label="Approximated wave", color="blue")
plt.plot(t,xt1, label="Rectangular wave", color="red")
plt.title(f"Approximation of rectangular signal using fourier series(n={n/2} terms)")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid()
plt.xticks(np.arange(-4*pi,4*pi,pi/2))
ax.xaxis.set_major_formatter(tick.FormatStrFormatter('%g$\pi$'))
ax.xaxis.set_major_locator(tick.MultipleLocator(base=1.0))

plt.legend(loc="best")
plt.show()