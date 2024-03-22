import matplotlib.pyplot as plt

# Define data
resource_counts = [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000]
init_times = [0.644, 0.650, 5.853, 0.838, 2.025, 0.863, 0.742, 0.830, 1.764, 0.755]
plan_times = [0.718, 1.090, 1.570, 2.201, 2.730, 3.194, 3.878, 8.854, 5.040, 10.082]
apply_times = [5.171, 13.931, 30.115, 45.140, 64.463, 87.743, 116.554, 151.255, 184.807, 229.146]
refresh_times = [0.479, 0.875, 1.388, 1.859, 2.250, 2.690, 3.466, 3.657, 4.683, 4.535]

# Create plots
plt.figure(figsize=(10, 6))

plt.plot(resource_counts, init_times, marker='o', label='init')
plt.plot(resource_counts, plan_times, marker='o', label='plan')
plt.plot(resource_counts, apply_times, marker='o', label='apply')
plt.plot(resource_counts, refresh_times, marker='o', label='refresh')

plt.title('Terraform Actions Time')
plt.xlabel('Resource Count')
plt.ylabel('Time (seconds)')
plt.grid(True)
plt.legend()
plt.xticks(resource_counts)
plt.tight_layout()

# Show plot
plt.show()