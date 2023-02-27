import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
# import scipy as sp

from scipy.optimize import minimize

data = [1, 0, 7, 8, 10]
data2 = np.random.randint(0, 10, 12)
# draw line
plt.plot(data, c='r', marker='o', linestyle='--', linewidth=2, markersize=12, markerfacecolor='g', markeredgecolor='b',
         markeredgewidth=3, antialiased=True)
x1 = 0
x2 = 5
y1 = 4
y2 = 4
plt.plot([x1, x2], [y1, y2], c='y')
# draw points
plt.scatter(range(len(data)), data, c='b')
# create labels
plt.xlabel('x Values')
plt.ylabel('y Values')
plt.title('Line Plot')

pd.DataFrame(data2).plot(kind='bar', color='r')
pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]).plot(kind='bar', color='g')
frame = pd.DataFrame({
    'id': [1, 2, 3],
    'name': ['a', 'b', 'c'],
    'age': [11, 12, 13]
})
print(frame)


# display
plt.show()
