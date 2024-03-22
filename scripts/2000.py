import matplotlib.pyplot as plt

# Data
categories = ['resource', 'module', 'resource + output', 'resource + added', 'resource + no refresh']
types = ['null_resource block', 'null_resource count', 'null_resource for_each',
         'MODULE BLOCK WITH NULL', 'MODULE BLOCK WITH COUNT ARGUMENT WITH NULL',
         'MODULE BLOCK WITH FOR_EACH ARGUMENT WITH NULL',
         'NULL WITH OUTPUT', 'NULL WITH COUNT WITH OUTPUT', 'NULL WITH COUNT WITH OUTPUT',
         'NULL UPDATED WITH SAME COUNT', 'NULL UPDATED WITH SAME COUNT USING COUNT ARGUMENT',
         'NULL UPDATED WITH SAME COUNT USING for_each ARGUMENT',
         'NULL UPDATED WITH SAME COUNT with no refresh',
         'NULL UPDATED WITH SAME COUNT with count with no refresh',
         'NULL UPDATED WITH SAME COUNT with for_each with no refresh']

init_real_time = [0.85, 0.797, 1.65, 1.431, 1.051, 1.123, 1.17, 0.997, 1.739, 4.469, 4.646, 0.738, 2.68, 1.235, 0.708]
plan_real_time = [1.673, 0.994, 6.897, 7.382, 5.42, 5.702, 16.276, 3.282, 6.908, 9.71, 6.847, 25.878, 8.792, 6.101, 24.128]
apply_real_time = [52.312, 24.141, 42.764, 89.153, 59.909, 61.81, 89.102, 31.264, 42.621, 194.765, 97.686, 131.99, 192.842, 97.492, 130.81]
refresh_real_time = [1.926, 2.145, 9.751, 8.172, 7.957, 7.857, 8.317, 4.629, 9.408, 9.716, 11.191, 31.18, 9.778, 11.169, 31.488]

# Plotting
fig, axs = plt.subplots(2, 1, figsize=(12, 12))

# Terraform plan and refresh graph
axs[0].bar(types, plan_real_time, label='Terraform Plan', color='b', alpha=0.6)
axs[0].bar(types, refresh_real_time, label='Terraform Refresh', color='g', alpha=0.6)
axs[0].set_ylabel('Time (s)')
axs[0].set_title('Terraform Plan and Refresh Times by Resource Type')
axs[0].legend()

# Terraform apply graph
axs[1].bar(types, apply_real_time, label='Terraform Apply', color='r', alpha=0.6)
axs[1].set_ylabel('Time (s)')
axs[1].set_title('Terraform Apply Times by Resource Type')

# Rotate x-axis labels for better visibility
for ax in axs:
    ax.set_xticklabels(types, rotation=90, ha='center')

plt.tight_layout()
plt.show()
