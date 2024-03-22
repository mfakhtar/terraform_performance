import matplotlib.pyplot as plt

# Data
resource_count = [500, 1000, 1500, 2000, 2500, 3000]
apply_real_time = [5.35, 15.218, 30.6, 52.312, 79.075, 112.247]
updated_resource_count = [1000, 2000, 3000, 4000, 5000, 6000]
updated_apply_real_time = [15.231, 52.761, 114.965, 194.765, 297.419, 435.531]

# Plotting
plt.figure(figsize=(10, 6))

plt.plot(resource_count, apply_real_time, marker='o', linestyle='-', color='blue', label='Before updating')
plt.plot(updated_resource_count, updated_apply_real_time, marker='s', linestyle='--', color='red', label='After updating')

plt.xlabel('Resource Count')
plt.ylabel('Apply Real Time (s)')
plt.title('Apply Real Time vs. Resource Count')
plt.legend()

plt.grid(True)
plt.tight_layout()
plt.show()
