import matplotlib.pyplot as plt

# Data for resource counts and corresponding durations
resource_counts = [0, 500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000, 7500, 8000, 8500, 9000]
plan_durations = [0.724, 0.75, 1.05, 1.479, 1.948, 2.719, 2.931, 3.724, 8.809, 9.541, 5.634, 0.13, 7.285, 10.535, 9.277, 10.259, 11.688, 12.629, 0.0]
apply_durations = [4.895, 5.131, 13.543, 25.343, 42.55, 63.726, 88.906, 116.67, 148.952, 190.055, 234.521, 281.718, 331.073, 390.514, 450.55, 507.731, 583.01, 663.729, 753.731]
refresh_durations = [0.14, 0.503, 0.839, 1.475, 1.889, 2.273, 2.691, 3.464, 3.611, 4.89, 5.012, 5.433, 5.921, 10.314, 7.41, 8.07, 8.686, 0.0, 0.0]

# Plotting the graph
plt.figure(figsize=(10, 6))

plt.plot(resource_counts, plan_durations, label='Plan', marker='o')
plt.plot(resource_counts, apply_durations, label='Apply', marker='o')
plt.plot(resource_counts, refresh_durations, label='Refresh', marker='o')

plt.xlabel('Resource Count')
plt.ylabel('Duration (seconds)')
plt.title('Terraform Operations Duration vs Resource Count')
plt.legend()
plt.grid(True)

plt.show()