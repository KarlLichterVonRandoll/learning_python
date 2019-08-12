import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

n = 500
x = np.random.normal(0, 1, n)
y = np.random.normal(0, 1, n)
z = np.random.normal(0, 1, n)
plt.figure('3D scatter')
ax3d = plt.gca(projection='3d')

d = x ** 2 + y ** 2 + z ** 2
ax3d.scatter(x, y, z, s=70, c=d,
             alpha=0.7, cmap='jet')
ax3d.set_xlabel('x')
ax3d.set_ylabel('y')
ax3d.set_zlabel('z')
plt.tight_layout()
plt.show()
