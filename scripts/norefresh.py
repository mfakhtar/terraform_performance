import matplotlib.pyplot as plt
import numpy as np

# Data
categories = [
    "resource",
    "resource",
    "resource",
    "resource + added",
    "resource + added",
    "resource + added",
    "resource + no refresh",
    "resource + no refresh",
    "resource + no refresh"
]

types = [
    "block",
    "count",
    "for_each",
    "block",
    "count",
    "for_each",
    "block",
    "count",
    "for_each"
]

#init_times = [0.85, 0.797, 1.65, 4.469, 4.646, 0.738, 2.68, 1.235, 0.708]

plan_times = [
    1.673, 0.994, 6.897, 9.71, 6.847, 25.878, 8.792, 6.101, 24.128
]

apply_times = [
    52.312, 24.141, 42.764, 194.765, 97.686, 131.99, 192.842, 97.492, 130.81
]

refresh_times = [
    1.926, 2.145, 9.751, 9.716, 11.191, 31.18, 9.778, 11.169, 31.488
]

# Plotting
fig, ax = plt.subplots(figsize=(12, 8))

bar_width = 0.2
index = np.arange(len(categories))

#bar1 = ax.bar(index, init_times, bar_width, label='Init Real Time (s)')
bar2 = ax.bar(index + bar_width, plan_times, bar_width, label='Plan Real Time (s)')
bar3 = ax.bar(index + 2 * bar_width, apply_times, bar_width, label='Apply Real Time (s)')
bar4 = ax.bar(index + 3 * bar_width, refresh_times, bar_width, label='Refresh Real Time (s)')

ax.set_xlabel('Resource Category + Type')
ax.set_ylabel('Time (s)')
ax.set_title('Terraform Times')
ax.set_xticks(index + 1.5 * bar_width)
ax.set_xticklabels([f"{cat}\n{typ}" for cat, typ in zip(categories, types)], rotation=45, ha='right')
ax.legend()

plt.tight_layout()
plt.show()
