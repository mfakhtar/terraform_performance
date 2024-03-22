import matplotlib.pyplot as plt

# Resource counts
resource_counts = [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000,
                   5500, 6000, 6500, 7000, 7500, 8000, 8500, 9000, 9500, 10000,
                   10500, 11000, 11500, 12000, 12500, 13000]

# Time taken for each command in seconds
init_times = [2.107, 0.607, 0.596, 0.609, 0.656, 2.569, 2.956, 0.796, 1.434, 0.74,
              0.694, 1.674, 1.704, 4.847, 4.937, 0.704, 1.017, 0.969, 590, 0.73,
              1.856, 2.337, 0.964, 0.954, 0.861, 1.844]

plan_times = [1.113, 1.068, 1.71, 2.139, 2.49, 3.035, 3.756, 4.364, 9.412, 10.155,
              6.004, 6.857, 10.45, 15.369, 12.454, 10.43, 11.32, 12.469, 13.531, 14.363,
              16.215, 16.757, 19.165, 18.96, 40.909, 37.813]

apply_times = [4.914, 13.577, 26.058, 43.015, 62.004, 87.779, 116.075, 146.42, 182.141,
               223.974, 265.279, 314.823, 3912.078, 7957.752, 8312.182, 10900.157,
               9362.4, 12961.944, 28756.415, 890.132, 9599.335, 10425.356, 11404.934,
               12776.096, 14136.226, 15005.37]

refresh_times = [0.506, 0.866, 1.455, 1.861, 2.067, 2.671, 3.133, 3.543, 5.036, 5.273,
                 5.854, 5.598, 10.313, 9.743, 932.598, 933.615, 8.953, 9.836, 12.872,
                 11.312, 11.019, 11.746, 12.641, 14.599, 26.15, 22.317]

# Plotting
plt.figure(figsize=(12, 8))

plt.plot(resource_counts, init_times, label='Init', marker='o')
plt.plot(resource_counts, plan_times, label='Plan', marker='o')
plt.plot(resource_counts, apply_times, label='Apply', marker='o')
plt.plot(resource_counts, refresh_times, label='Refresh', marker='o')

plt.title('Terraform Time vs Resource Count')
plt.xlabel('Resource Count')
plt.ylabel('Time (seconds)')
plt.grid(True)
plt.legend()

plt.xticks(resource_counts, rotation=45)
plt.tight_layout()

plt.show()