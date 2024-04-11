import matplotlib.pyplot as plt
import numpy as np

# Sample data
correct1 = [15, 20, 20, 19, 17, 18, 17, 19, 13, 12, 7, 17]
wrong1 = [7, 2, 2, 3, 5, 4, 5, 3, 9, 10, 15, 5]
correct2 = [14, 18, 20, 20, 18, 18, 17, 18, 14, 15, 7, 13]
wrong2 = [8, 3, 2, 2, 4, 4, 5, 4, 8, 7, 9, 9]
correct3 = [17, 19, 22, 20, 20, 15, 17, 17, 14, 15, 13, 13]
wrong3 =[5, 3, 0, 2, 2, 7, 3, 5, 8, 7, 13, 9]
colours = ['red', 'orange', 'yellow', 'green', 'skyblue', 'bright_blue', 'purple', 'lilac', 'steel', 'rose', 'deep_red', 'blue']

# Setting up the figure size for better visibility
# Define figure size to accommodate all bars clearly
fig, ax = plt.subplots(figsize=(20, 10))

# Define bar width and the number of groups
bar_width = 0.15
n_groups = len(colours)

# Calculate the total width for each group (correct + wrong) and the space between groups
group_width = bar_width * 2
space_between_groups = bar_width

# Set the positions of the bars
index = np.arange(0, n_groups * (group_width + space_between_groups), group_width + space_between_groups)

# Define colors for correct and wrong for visual distinction
colors_correct = ['lightblue', 'lightgreen', 'lightcoral']
colors_wrong = ['blue', 'green', 'red']

# Plot the bars for each group
for i in range(3):  # Assuming there are 3 'correct' and 3 'wrong' sets
    correct = eval(f'correct{i+1}')
    wrong = eval(f'wrong{i+1}')
    ax.bar(index + i * bar_width, correct, bar_width, label=f'Correct {i+1}', color=colors_correct[i])
    ax.bar(index + i * bar_width + bar_width, wrong, bar_width, label=f'Wrong {i+1}', color=colors_wrong[i])

# Set the labels, titles, and ticks for the chart
ax.set_xlabel('Colors', fontsize=14)
ax.set_ylabel('Revenue', fontsize=14)
ax.set_title('Revenue by Color and Correctness', fontsize=16)
ax.set_xticks(index + group_width / 2)
ax.set_xticklabels(colours)

# Add a legend
ax.legend()

# Show the plot with a tight layout
plt.tight_layout()
plt.show()