import numpy as np
from matplotlib import pyplot as plt

t = np.arange(-1,1,0.01)
xt = np.sin(2*np.pi*t)
xt2 = [1 if i>=0 else 0 for i in t]
# plt.plot(t,xt)
# plt.title("Sin wave")

plt.plot(t,xt2)
plt.title("Unit step signal")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.show()