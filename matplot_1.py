import numpy as np
import scipy
import sys
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
x = np.array([1, 2, 3, 4])
y = np.array([1, 4, 9, 16])
z=np.array([4,5,2,23])
fig=plt.figure()
Ax=fig.add_subplot(111,projection="3d")

plt.plot(x, y)
plt.xlabel('X-axis label')
plt.ylabel('Y-axis label')
plt.title('Title of the graph')
plt.show()


#Two  lines to make our compiler able to draw:
plt.savefig("plot.png")
sys.stdout.flush()


