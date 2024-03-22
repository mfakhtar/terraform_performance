import matplotlib.pyplot as plt

# Data from the input
resource_counts = [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000]
init_times = [1.454, 0.871, 0.742, 0.738, 2.226, 0.904, 0.847, 0.763, 1.818, 0.689, 0.806, 2.731]
plan_times = [0.723, 1.092, 1.505, 1.951, 2.464, 3.197, 3.690, 4.092, 4.711, 5.337, 6.209, 6.874]
apply_times = [5.023, 12.745, 24.639, 42.648, 61.701, 88.326, 116.121, 147.163, 180.927, 225.250, 265.812, 315.751]
refresh_times = [0.577, 0.861, 1.218, 1.666, 2.040, 2.456, 2.994, 3.357, 3.934, 4.323, 4.865, 5.584]

# Plotting
plt.figure(figsize=(10, 8))

plt.plot(resource_counts, init_times, marker='o', linestyle='-', label='Init')
plt.plot(resource_counts, plan_times, marker='s', linestyle='-', label='Plan')
plt.plot(resource_counts, apply_times, marker='^', linestyle='-', label='Apply')
plt.plot(resource_counts, refresh_times, marker='x', linestyle='-', label='Refresh')

plt.xlabel('Resource Count')
plt.ylabel('Real Time (seconds)')
plt.title('Terraform Operations Time vs. Resource Count')
plt.legend()
plt.grid(True)

plt.show()