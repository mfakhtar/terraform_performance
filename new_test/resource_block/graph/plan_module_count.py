import pandas as pd
import matplotlib.pyplot as plt

# Provided data
data = {
    'Count': [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000],
    'Type': ['null_resource module with count'] * 10,
#    'Init Real Time (s)': [1.123, 3.299, 1.179, 1.051, 1.045, 1.039, 0.953, 1.039, 1.008, 1.105],
    'Plan Real Time (s)': [1.888, 2.843, 4.013, 5.42, 7.132, 9.047, 11.879, 14.342, 17.919, 21.521],
#    'Apply Real Time (s)': [6.768, 18.447, 35.807, 59.909, 90.155, 128.61, 172.809, 220.053, 278.919, 341.518],
    'Refresh Real Time (s)': [1.801, 3.065, 5.114, 7.957, 10.955, 15.287, 20.265, 26.108, 33.39, 41.032]
}

# Creating DataFrame
df = pd.DataFrame(data)

# Plotting
plt.figure(figsize=(10, 6))

#plt.plot(df['Count'], df['Init Real Time (s)'], marker='o', label='Init Real Time')
plt.plot(df['Count'], df['Plan Real Time (s)'], marker='o', label='Plan Real Time')
#plt.plot(df['Count'], df['Apply Real Time (s)'], marker='o', label='Apply Real Time')
plt.plot(df['Count'], df['Refresh Real Time (s)'], marker='o', label='Refresh Real Time')

plt.title('Terraform Execution Time with null_resource module with count')
plt.xlabel('Count')
plt.ylabel('Time (s)')
plt.legend()
plt.grid(True)
plt.xticks(df['Count'])

plt.tight_layout()
plt.show()
