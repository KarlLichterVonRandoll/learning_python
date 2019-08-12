import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

n = 500
x, y = np.meshgrid(np.linspace(-3, 3, n),
                   np.linspace(-3, 3, n))
z = (1 - x / 2 + x ** 5 + y ** 3) * np.exp(-x ** 2 - y ** 2)

plt.figure('3D surface')
ax3d = plt.gca(projection='3d')

d = x ** 2 + y ** 2 + z ** 2
ax3d.plot_wireframe(x, y, z,
                    rstride=10,
                    cstride=10,
                    cmap='jet',
                    linewidth=1)
ax3d.set_xlabel('x')
ax3d.set_ylabel('y')
ax3d.set_zlabel('z')
plt.tight_layout()
plt.show()
