import matplotlib.pyplot as plt

# Data
categories = [
    "resource",
    "resource",
    "resource",
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

# Calculate percentage difference compared to block type within each category for plan and refresh
block_indices = [i for i, typ in enumerate(types) if typ == "block"]
percentage_difference_within_category = [
    ((plan_times[i] - plan_times[block_indices[c]]) / plan_times[block_indices[c]]) * 100
#    if i != block_indices[c] else 0
    for c, i in enumerate(range(len(types)))
]

block_indices = [i for i, typ in enumerate(types) if typ == "block"]
percentage_difference_within_category = [
    ((refresh_times[i] - refresh_times[block_indices[c]]) / refresh_times[block_indices[c]]) * 100
#    if i != block_indices[c] else 0
    for c, i in enumerate(range(len(types)))
]


# ========================

# Plotting plan times
plt.figure(figsize=(12, 8))

bars_plan = plt.bar(range(len(categories)), plan_times, color='skyblue')

# Adding percentage labels for plan times
for i, bar in enumerate(bars_plan):
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, height, f'{percentage_difference_within_category_plan[i]:.1f}%',
             ha='center', va='bottom', color='black', fontsize=9)

plt.xlabel('Resource Category + Type')
plt.ylabel('Time (s)')
plt.title('Terraform Plan Times')

plt.xticks(range(len(categories)), [f"{cat}\n{typ}" for cat, typ in zip(categories, types)], rotation=45, ha='right')

plt.tight_layout()
plt.show()

# Plotting refresh times
plt.figure(figsize=(12, 8))

bars_refresh = plt.bar(range(len(categories)), refresh_times, color='skyblue')

# Adding percentage labels for refresh times
for i, bar in enumerate(bars_refresh):
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, height, f'{percentage_difference_within_category_refresh[i]:.1f}%',
             ha='center', va='bottom', color='black', fontsize=9)

plt.xlabel('Resource Category + Type')
plt.ylabel('Time (s)')
plt.title('Terraform Refresh Times')

plt.xticks(range(len(categories)), [f"{cat}\n{typ}" for cat, typ in zip(categories, types)], rotation=45, ha='right')

plt.tight_layout()
plt.show()


