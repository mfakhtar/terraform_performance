import matplotlib.pyplot as plt

# Data
categories = [
    "resource",
    "resource",
    "resource",
    "resource + added",
    "resource + added",
    "resource + added"
]

types = [
    "block",
    "count",
    "for_each",
    "block",
    "count",
    "for_each"
]

#init_times = [
#    0.85, 0.797, 1.65, 4.469, 4.646, 0.738
#]

plan_times = [
    1.673, 0.994, 6.897, 9.71, 6.847, 25.878
]

apply_times = [
    52.312, 24.141, 42.764, 194.765, 97.686, 131.99
]

refresh_times = [
    1.926, 2.145, 9.751, 9.716, 11.191, 31.18
]

# Plotting
fig, ax = plt.subplots(figsize=(12, 8))

bar_width = 0.2
index = range(len(categories))

#bar1 = ax.bar(index, init_times, bar_width, label='Init Real Time (s)')
bar2 = ax.bar([i + bar_width for i in index], plan_times, bar_width, label='Plan Real Time (s)')
bar3 = ax.bar([i + 2 * bar_width for i in index], apply_times, bar_width, label='Apply Real Time (s)')
bar4 = ax.bar([i + 3 * bar_width for i in index], refresh_times, bar_width, label='Refresh Real Time (s)')

ax.set_xlabel('Resource Category + Type')
ax.set_ylabel('Time (s)')
ax.set_title('Terraform Times doubling the resources')
ax.set_xticks([i + 1.5 * bar_width for i in index])
ax.set_xticklabels([f"{cat}\n{typ}" for cat, typ in zip(categories, types)], rotation=45, ha='right')
ax.legend()

plt.tight_layout()
plt.show()
