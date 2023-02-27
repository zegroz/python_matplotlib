import matplotlib.pyplot as plt
import numpy as np

species = ("Max", "Musterman", "Test", "Test2")
data = {
    'Blau': (5.6, 7.9, 9.1, 10),
    'Orange': (18.3, 18.7, 19.3, 25),
    'Green': (88.9, 88.1, 88.5, 100),
}

x = np.arange(len(species))  # the label locations
width = 0.25  # the width of the bars
multiplier = 0

fig, ax = plt.subplots(constrained_layout=True)

for attribute, value in data.items():
    print(f"Attribute: {attribute}, value: {value}")
    offset = width * multiplier
    rects = ax.bar(x + offset, value, width, label=attribute)
    ax.bar_label(rects, padding=3)
    multiplier += 1

ax.set_ylabel('Length (mm)')
ax.set_xlabel('Person')
ax.set_title('Test values')
ax.set_xticks(x + width, species)
ax.legend(loc='upper left', ncols=3)
ax.set_ylim(0, 250)

plt.show()
