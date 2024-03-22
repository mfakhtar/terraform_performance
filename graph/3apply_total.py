import matplotlib.pyplot as plt

# Data
configurations = ['1000 resource blocks', '1000 resource with count', '1000 resource with for_each']
apply_times = [13.416, 8.221, 9.775]
apply_module_times = [15.838, 11.432, 11.381]
apply_output_times = [14.664, 7.966, 9.613]
apply_double_times = [29.132, 15.398, 20.241]

# Plotting
barWidth = 0.2
x = range(len(configurations))

plt.bar(x, apply_times, color='b', width=barWidth, label='terraform apply')
plt.bar([i + barWidth for i in x], apply_module_times, color='g', width=barWidth, label='terraform apply with Module')
plt.bar([i + barWidth*2 for i in x], apply_output_times, color='r', width=barWidth, label='terraform apply with output')
plt.bar([i + barWidth*3 for i in x], apply_double_times, color='y', width=barWidth, label='terraform apply with double resource updation')

plt.xlabel('Configurations')
plt.ylabel('Total Time (s)')
plt.title('Terraform Apply Times for Different Configurations')
plt.xticks([i + barWidth*1.5 for i in x], configurations, rotation=45)
plt.legend()

plt.tight_layout()
plt.show()