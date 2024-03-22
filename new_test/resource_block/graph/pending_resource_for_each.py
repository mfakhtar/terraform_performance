import pandas as pd
import matplotlib.pyplot as plt

# Provided data
data = {
    'Count': [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000],
    'Type': ['null_resource for_each'] * 10,
    'Init Real Time (s)': [0.699, 4.483, 1.834, 1.65, 1.728, 1.688, 6.682, 1.622, 2.231, 9.899],
    'Plan Real Time (s)': [5.835, 3.182, 4.5, 6.048, 7.872, 9.712, 11.927, 14.585, 17.081, 19.982],
    'Apply Real Time (s)': [5.934, 3.184, 4.508, 6.02, 7.858, 9.715, 11.854, 14.455, 16.854, 19.641],
    'Refresh Real Time (s)': [5.836, 3.192, 4.476, 6.074, 7.763, 9.734, 11.898, 14.341, 16.714, 19.818]
}

# Creating DataFrame
df = pd.DataFrame(data)

# Plotting
plt.figure(figsize=(10, 6))

plt.plot(df['Count'], df['Init Real Time (s)'], marker='o', label='Init Real Time')
plt.plot(df['Count'], df['Plan Real Time (s)'], marker='o', label='Plan Real Time')
plt.plot(df['Count'], df['Apply Real Time (s)'], marker='o', label='Apply Real Time')
plt.plot(df['Count'], df['Refresh Real Time (s)'], marker='o', label='Refresh Real Time')

plt.title('Terraform Execution Time with null_resource for_each')
plt.xlabel('Count')
plt.ylabel('Time (s)')
plt.legend()
plt.grid(True)
plt.xticks(df['Count'])

plt.tight_layout()
plt.show()