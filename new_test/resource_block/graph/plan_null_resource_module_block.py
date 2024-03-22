import pandas as pd
import matplotlib.pyplot as plt

# Provided data
data = {
    'Count': [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000],
    'Type': ['null_resource module'] * 10,
#    'Init Real Time (s)': [1.22, 1.213, 1.466, 1.431, 1.563, 1.719, 2.22, 2.2, 5.462, 2.487],
    'Plan Real Time (s)': [2.471, 3.776, 5.536, 7.382, 9.821, 12.17, 16.251, 18.082, 21.665, 25.33],
#    'Apply Real Time (s)': [8.756, 27.191, 52.152, 89.153, 136.648, 193.332, 263.284, 337.489, 422.047, 519.665],
    'Refresh Real Time (s)': [2.005, 3.982, 5.742, 8.172, 11.835, 14.253, 18.715, 22.161, 26.527, 30.765]
}

# Creating DataFrame
df = pd.DataFrame(data)

# Plotting
plt.figure(figsize=(10, 6))

#plt.plot(df['Count'], df['Init Real Time (s)'], marker='o', label='Init Real Time')
plt.plot(df['Count'], df['Plan Real Time (s)'], marker='o', label='Plan Real Time')
#plt.plot(df['Count'], df['Apply Real Time (s)'], marker='o', label='Apply Real Time')
plt.plot(df['Count'], df['Refresh Real Time (s)'], marker='o', label='Refresh Real Time')

plt.title('Terraform Execution Time with null_resource module')
plt.xlabel('Count')
plt.ylabel('Time (s)')
plt.legend()
plt.grid(True)
plt.xticks(df['Count'])

plt.tight_layout()
plt.show()