import matplotlib.pyplot as plt

# Data
resource_counts = [10, 100, 1000]  # Common resource counts for simplicity
# Times for terraform apply - regular blocks
apply_times_regular = [0.254, 0.963, 13.416]
# Times for terraform apply - with count argument
apply_times_count = [0.242, 0.781, 8.221]
# Times for terraform apply - with for_each argument
apply_times_foreach = [0.227, 1.081, 9.775]

# Create the plot
plt.figure(figsize=(10, 6))

# Plot each category with different markers and colors
plt.plot(resource_counts, apply_times_regular, marker='o', linestyle='-', color='b', label='Regular Blocks')
plt.plot(resource_counts, apply_times_count, marker='s', linestyle='--', color='r', label='With Count Argument')
plt.plot(resource_counts, apply_times_foreach, marker='^', linestyle='-.', color='g', label='With For-Each Argument')

# Add title and labels
plt.title('Terraform Apply Time vs Resource Count')
plt.xlabel('Resource Count')
plt.ylabel('Apply Time (seconds)')

# Show grid and legend
plt.grid(True)
plt.legend()

# Display the plot
plt.show()