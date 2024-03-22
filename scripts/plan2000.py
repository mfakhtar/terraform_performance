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
    "resource + output",
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
    "BLOCK WITH NULL",
    "BLOCK WITH COUNT ARGUMENT WITH NULL",
    "BLOCK WITH FOR_EACH ARGUMENT WITH NULL",
    "NULL WITH OUTPUT",
    "NULL WITH COUNT WITH OUTPUT",
    "NULL WITH COUNT WITH OUTPUT",
    "UPDATED WITH SAME COUNT",
    "UPDATED WITH SAME COUNT USING COUNT ARGUMENT",
    "UPDATED WITH SAME COUNT USING for_each ARGUMENT",
    "UPDATED WITH SAME COUNT with no refresh",
    "UPDATED WITH SAME COUNT with count with no refresh",
    "UPDATED WITH SAME COUNT with for_each with no refresh"
]

init_times = [
    0.85, 0.797, 1.65, 1.431, 1.051, 1.123, 1.17, 0.997, 1.739, 4.469, 4.646, 0.738, 2.68, 1.235, 0.708
]

plan_times = [
    1.673, 0.994, 6.897, 7.382, 5.42, 5.702, 16.276, 3.282, 6.908, 9.71, 6.847, 25.878, 8.792, 6.101, 24.128
]

refresh_times = [
    52.312, 24.141, 42.764, 89.153, 59.909, 61.81, 89.102, 31.264, 42.621, 194.765, 97.686, 131.99, 192.842, 97.492, 130.81
]

# Plotting
fig, ax = plt.subplots(figsize=(14, 8))

bar_width = 0.25
index = range(len(categories))

bar1 = ax.bar(index, init_times, bar_width, label='Init Real Time (s)')
bar2 = ax.bar([i + bar_width for i in index], plan_times, bar_width, label='Plan Real Time (s)')
bar3 = ax.bar([i + 2*bar_width for i in index], refresh_times, bar_width, label='Refresh Real Time (s)')

ax.set_xlabel('Resource Category + Type')
ax.set_ylabel('Time (s)')
ax.set_title('Terraform Plan and Refresh Times')
ax.set_xticks([i + bar_width for i in index])
ax.set_xticklabels([f"{cat}\n{typ}" for cat, typ in zip(categories, types)], rotation=45, ha='right')
ax.legend()

plt.tight_layout()
plt.show()
