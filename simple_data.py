import matplotlib.pyplot as plt
import numpy as np

#print(plt.style.available)
#plt.xkcd() # Comic style
plt.style.use('seaborn-v0_8') # 'seaborn', 'ggplot', 'dark_background', 'bmh', 'fivethirtyeight', 'grayscale'
data1_x = np.arange(0, 6, 1) # von 0 bis 6 mit Schrittweite 1
data1_y = np.arange(0, 6, 1)
plt.plot(data1_x, data1_y, label='Simple data 1', linewidth=4)
plt.bar(data1_x, data1_y, label='Simple data 1 (bar)', linewidth=4, color='#e5ae38')

x1 = 0
x2 = 11
y1 = 5.5
y2 = 5.5
plt.plot([x1, x2], [y1, y2], c='r', linestyle='--')

data2_x = [6, 7, 8, 9, 10, 11] 
data2_y = [6, 7, 8, 9, 10, 11]
plt.plot(data2_x, data2_y, label='Simple data 2', linewidth=4)
plt.bar(data2_x, data2_y, label='Simple data 2', linewidth=4, color='#444444')

plt.xlabel('x Werte')
plt.ylabel('y Werte')
plt.title('Line Plot')
plt.legend() # ['Simple data 1=data1', 'Simple data 2=data2']
plt.grid(True)
plt.xticks(np.arange(1, 15, 1)) 
plt.yticks(np.arange(1, 15, 1))

plt.tight_layout() # padding
plt.show()

