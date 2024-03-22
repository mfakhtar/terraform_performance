import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['resource_block', 'resource_count', 'resource_for_each',
              'module_block', 'module_count', 'module_for_each',
              'resource_output_block', 'resource_output_count', 'resource_output_for_each']

plan_times = [1.673, 0.994, 6.897, 7.382, 5.42, 5.702, 16.276, 3.282, 6.908]
apply_times = [52.312, 24.141, 42.764, 89.153, 59.909, 61.81, 89.102, 31.264, 42.621]
refresh_times = [1.926, 2.145, 9.751, 8.172, 7.957, 7.857, 8.317, 4.629, 9.408]
state_file_sizes = [766, 455, 459, 827, 848, 869, 933, 542, 631]

# Plotting
bar_width = 0.2
index = np.arange(len(categories))

plt.figure(figsize=(12, 8))

plt.bar(index - bar_width, plan_times, bar_width, label='Plan Real Time')
plt.bar(index, apply_times, bar_width, label='Apply Real Time')
plt.bar(index + bar_width, refresh_times, bar_width, label='Refresh Real Time')

plt.xlabel('Category - Type')
plt.ylabel('Time (s) / State File Size (KB)')
plt.title('Terraform Real Time and State File Size by Category and Type')
plt.xticks(index, categories, rotation=45, ha='right')
plt.legend()

# Secondary Y-axis for State File Size
ax2 = plt.gca().twinx()
ax2.plot(index, state_file_sizes, color='orange', marker='o', linestyle='--', label='State File Size (KB)')
ax2.set_ylabel('State File Size (KB)')
ax2.legend(loc='upper left')

plt.tight_layout()
plt.show()
