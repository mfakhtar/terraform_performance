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

# Plotting
plt.figure(figsize=(10, 6))

plt.bar(range(len(categories)), apply_times, color='skyblue')

plt.xlabel('Resource Category + Type')
plt.ylabel('Time (s)')
plt.title('Terraform Apply Times')

plt.xticks(range(len(categories)), [f"{cat}\n{typ}" for cat, typ in zip(categories, types)], rotation=45, ha='right')

plt.tight_layout()
plt.show()
