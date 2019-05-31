# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
import cv2


fig = plt.figure()
ax = fig.gca(projection='3d')

# Make data.
file_path = r"D:\CNN\ttt\6.png"
data = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
data = np.array(data)
shape = np.shape(data)



h = shape[0]
w = shape[1]
print(h)

X = np.arange(0, w, 1)
Y = np.arange(0, h, 1)
X, Y = np.meshgrid(X, Y)
Z = data

# Plot the surface.
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.get_cmap("rainbow"),
                       linewidth=0, antialiased=False)

# Customize the z axis.
ax.set_zlim(20, 255)
#z轴网格线的疏密，刻度的疏密，10表示刻度的个数
ax.zaxis.set_major_locator(LinearLocator(10))
#z轴的刻度保留小数点后的位数
ax.zaxis.set_major_formatter(FormatStrFormatter("%.01d"))

#设置坐标轴的label和标题
ax.set_xlabel("X", size=15)
ax.set_ylabel("Y", size=15)
ax.set_zlabel("Z", size=15)
#ax.set_title("Title", weight="bold",size=20,)


# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)
#shrink表示整体收缩比例，aspect值越大，bar越窄

plt.show()
