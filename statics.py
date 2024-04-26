import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

a = [20, 25, 27, 25, 22, 22, 21, 23, 17, 15, 12, 20]
b = [10, 5, 3, 5, 8, 8, 9, 7, 13, 15, 18, 10]

#a2 = [20, 25, 28, 28, 25, 24, 22, 24, 19, 20, 9, 17]
#b2 = [10, 5, 2, 2, 5, 6, 8, 6, 11, 10, 21, 13]

#a3 = [20, 27, 28, 28, 25, 19, 25, 22, 19, 20, 11, 16]
#b3 = [10, 3, 2, 2, 5, 11, 5, 8, 11, 10, 19, 14]

#at = [60, 77, 83, 81, 72, 65, 68, 69, 55, 55, 32, 53]
#bt = [30, 13, 7, 9, 18, 25, 22, 21, 35, 35, 58, 36]

colour = ['red(C)', 'orange(G)', 'yellow(D)', 'green(A)', 'skyblue(E)', 'blue(B)', 'bright_blue(Gb)', 'purple(Db)', 'lilac(Ab)', 'steel(Eb)', 'rose(Bb)', 'deep_red(F)']

df = pd.DataFrame({'correct': a, 'incorrect': b}, index=colour)

# Set figure size and bar width
fig, ax = plt.subplots(figsize=(15, 8))
bar_width = 0.35

# Positioning indexes for bars
index = np.arange(len(colour))

# Plot bars
b1 = ax.bar(index, df['correct'], bar_width, alpha=0.4, color='green', label='Correct')
b2 = ax.bar(index + bar_width, df['incorrect'], bar_width, alpha=0.4, color='orange', label='Incorrect')

# Function to add value labels on the bars
def add_value_labels(ax, bars, spacing=5):
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height, f'{int(height)}',
                ha='center', va='bottom', fontsize=12, color='black', fontweight='bold', rotation='horizontal')

# Add labels to the bars
add_value_labels(ax, b1, spacing=8)
add_value_labels(ax, b2, spacing=8)

# Setting x-axis details
ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels(colour, fontsize=10, color='black', rotation=45, ha='right')

# Set axes labels and legend
ax.set_xlabel('Colour First', size=13)
ax.set_ylabel('Counts', size=13)
ax.legend()

plt.tight_layout()
plt.savefig("plot.svg", format='svg')  # Saving the figure as an SVG file
plt.show()