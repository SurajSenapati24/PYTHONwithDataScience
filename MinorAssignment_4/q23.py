import matplotlib.pyplot as plt
from collections import Counter

# Given list of responses
responses = [1, 2, 5, 4, 3, 5, 2, 1, 3, 3, 1, 4, 3, 3, 3, 2, 3, 3, 2, 5]

# Count the frequency of each response
response_counts = Counter(responses)

# Calculate percentages
total_responses = len(responses)
percentages = {key: (value / total_responses) * 100 for key, value in response_counts.items()}

# Data for the bar chart
labels = list(response_counts.keys())
counts = list(response_counts.values())
percents = [percentages[label] for label in labels]

# Plotting the bar chart
fig, ax = plt.subplots()
ax.bar(labels, counts, color='skyblue')

# Adding the percentages as text on top of each bar
for i, v in enumerate(counts):
    ax.text(labels[i], v + 0.2, f'{percents[i]:.2f}%', ha='center', va='bottom', fontsize=10)

# Setting the title and labels
ax.set_title("Response Frequencies and Percentages", fontsize=14)
ax.set_xlabel("Response", fontsize=12)
ax.set_ylabel("Frequency", fontsize=12)

# Display the chart
plt.show()
