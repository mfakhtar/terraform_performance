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

apply_times = [
    52.312,
    24.141,
    42.764,
    89.153,
    59.909,
    61.81,
    89.102,
    31.264,
    42.621
]

# Calculate percentage difference compared to block type within each category
block_indices = [i for i, typ in enumerate(types) if typ == "block"]
percentage_difference_within_category = [
    ((apply_times[i] - apply_times[block_indices[c]]) / apply_times[block_indices[c]]) * 100
    if i != block_indices[c] else 0
    for c, i in enumerate(range(len(types)))
]

# Plotting
plt.figure(figsize=(12, 8))

bars = plt.bar(range(len(categories)), apply_times, color='skyblue')

# Adding percentage labels
for i, bar in enumerate(bars):
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, height, f'{percentage_difference_within_category[i]:.1f}%',
             ha='center', va='bottom', color='black', fontsize=9)

plt.xlabel('Resource Category + Type')
plt.ylabel('Time (s)')
plt.title('Terraform Apply Times')

plt.xticks(range(len(categories)), [f"{cat}\n{typ}" for cat, typ in zip(categories, types)], rotation=45, ha='right')

plt.tight_layout()
plt.show()
