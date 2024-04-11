import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

a = [20, 25, 27, 25, 22, 22, 21, 23, 17, 15, 12, 20]
b = [10, 5, 3, 5, 8, 8, 9, 7, 13, 15, 18, 9]

#a2 = [20, 25, 28, 28, 25, 24, 22, 24, 19, 20, 9, 17]
#b2 = [10, 5, 2, 2, 5, 6, 8, 6, 11, 10, 21, 13]

#a3 = [20, 27, 28, 28, 25, 19, 25, 22, 19, 20, 11, 16]
#b3 = [10, 3, 2, 2, 5, 5, 11, 5, 8, 11, 10, 19, 14]

#at = [60, 77, 83, 81, 72, 65, 68, 69, 55, 55, 32, 53]
#bt = [30, 13, 7, 9, 18, 25, 22, 21, 35, 35, 58, 36]

colour = ['red(C)', 'orange(G)', 'yellow(A)', 'green(D)', 'skyblue(E)', 'blue(B)', 'bright_blue(Gb)', 'purple(Db)', 'lilac(Ab)', 'steel(Eb)', 'rose(Bb)', 'deep_red(F)']

df = pd.DataFrame({'correct': a, 'incorrect': b}, index=colour)

# 그림 사이즈, 바 굵기 조정
fig, ax = plt.subplots(figsize=(12, 6))
bar_width = 0.25

# Positioning indexes for bars
index = np.arange(len(colour))

# Plot bars
b1 = plt.bar(index, df['correct'], bar_width, alpha=0.4, color='blue', label='Correct')
b2 = plt.bar(index + bar_width, df['incorrect'], bar_width, alpha=0.4, color='red', label='Incorrect')

# Adding labels to each bar in b1 and b2
for bars in [b1, b2]:
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, height, f'{height:.1f}', ha='center', va='bottom', size=12)

# Setting x-axis details
plt.xticks(index + bar_width / 2, colour)  # Center labels between bars

# Set axes labels and legend
plt.xlabel('Colour', size=13)
plt.ylabel('Counts', size=13)
plt.legend()
plt.show()