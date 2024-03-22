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

# Calculate percentage difference compared to resource block
resource_block_apply_time = apply_times[0]
percentage_difference = [(time - resource_block_apply_time) / resource_block_apply_time * 100 for time in apply_times]

# Plotting
plt.figure(figsize=(10, 6))

bars = plt.bar(range(len(categories)), apply_times, color='skyblue')

# Adding percentage labels
for i, bar in enumerate(bars):
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, height, f'{percentage_difference[i]:.1f}%',
             ha='center', va='bottom', color='black', fontsize=9)

plt.xlabel('Resource Category + Type')
plt.ylabel('Time (s)')
plt.title('Terraform Apply Times for 2000 null_resource')

plt.xticks(range(len(categories)), [f"{cat}\n{typ}" for cat, typ in zip(categories, types)], rotation=45, ha='right')

plt.tight_layout()
plt.show()
