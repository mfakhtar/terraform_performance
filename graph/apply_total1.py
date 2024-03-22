import matplotlib.pyplot as plt

# Data
resource_counts = [10, 100, 1000]  # Resource counts
apply_times_regular = [0.254, 0.963, 13.416]  # Total times for terraform apply - Regular resource
apply_times_module = [0.249, 0.989, 14.664]  # Total times for terraform apply - Resource with Module
apply_times_output = [0.249, 1.099, 14.664]  # Total times for terraform apply - Resource with Output
apply_times_double_addition = [0.263, 1.060, 29.132]  # Total times for terraform apply - Double resources addition

# Create the plot
plt.figure(figsize=(10, 6))

# Plot each category
plt.plot(resource_counts, apply_times_regular, marker='o', linestyle='-', color='b', label='Regular Resource')
plt.plot(resource_counts, apply_times_module, marker='s', linestyle='--', color='r', label='Resource with Module')
plt.plot(resource_counts, apply_times_output, marker='^', linestyle='-.', color='g', label='Resource with Output')
plt.plot(resource_counts, apply_times_double_addition, marker='d', linestyle=':', color='purple', label='Double Resources Addition')

# Add title and labels
plt.title('Terraform Apply Time vs Resource Count')
plt.xlabel('Resource Count')
plt.ylabel('Apply Time (seconds)')

# Show grid and legend
plt.grid(True)
plt.legend()

# Display the plot
plt.show()
