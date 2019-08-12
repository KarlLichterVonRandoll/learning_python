import numpy as np
import matplotlib.pyplot as plt

plt.figure("Polar", facecolor="lightgray")
plt.title("Polar")

plt.gca(projection='polar')
plt.title('Polar')
plt.xlabel(r'$\theta$', fontsize=14)
plt.ylabel(r'$\rho$', fontsize=14)
plt.grid(linestyle=':')
#  绘制图像
t = np.linspace(0, 4*np.pi, 1000)
r = 0.8 * t
plt.plot(t, r)

x = np.linspace(0, 6*np.pi, 1000)
y = 3*np.sin(8*x)
plt.plot(x, y)
plt.show()