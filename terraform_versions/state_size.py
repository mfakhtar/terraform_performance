import matplotlib.pyplot as plt

# Data
categories = ['resource_block', 'resource_count', 'resource_for_each',
              'module_block', 'module_count', 'module_for_each',
              'resource_output_block', 'resource_output_count', 'resource_output_for_each']
file_sizes = [766, 455, 459, 827, 848, 869, 933, 542, 631]
bar_colors = ['blue', 'orange', 'green', 'red', 'purple', 'brown', 'pink', 'gray', 'cyan']

# Plotting
plt.figure(figsize=(10, 6))
plt.bar(categories, file_sizes, color=bar_colors)

# Adding labels and titles
plt.xlabel('Category - Type')
plt.ylabel('State File Size (KB)')
plt.title('Terraform State File Size by Category and Type')

# Show the plot
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
