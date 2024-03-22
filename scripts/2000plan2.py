import matplotlib.pyplot as plt

# Data
categories = [
    "null_resource",
    "null_resource",
    "null_resource",
    "module",
    "module",
    "module",
    "resource + output",
    "resource + output",
    "resource + output"
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

plan_times = [
    1.673, 0.994, 6.897, 7.382, 5.42, 5.702, 16.276, 3.282, 6.908
]

refresh_times = [
    1.926, 2.145, 9.751, 8.172, 7.957, 7.857, 8.317, 4.629, 9.408
]

# Plotting
fig, ax = plt.subplots(figsize=(12, 8))

bar_width = 0.35
index = range(len(categories))

bar1 = ax.bar(index, plan_times, bar_width, label='Plan Real Time (s)')
bar2 = ax.bar([i + bar_width for i in index], refresh_times, bar_width, label='Refresh Real Time (s)')

ax.set_xlabel('Resource Category + Type')
ax.set_ylabel('Time (s)')
ax.set_title('Terraform Plan and Refresh Times for 2000 null_resource')
ax.set_xticks([i + bar_width / 2 for i in index])
ax.set_xticklabels([f"{cat}\n{typ}" for cat, typ in zip(categories, types)], rotation=45, ha='right')
ax.legend()

plt.tight_layout()
plt.show()
