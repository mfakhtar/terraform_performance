import pandas as pd
import matplotlib.pyplot as plt

# Provided data
data = {
    'Count': [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000],
    'Type': ['null_resource with output block'] * 10,
    'Init Real Time (s)': [5.179, 1.085, 1.223, 1.17, 1.148, 1.238, 1.249, 1.235, 1.31, 1.398],
    'Plan Real Time (s)': [3.069, 5.602, 9.702, 16.276, 24.104, 33.869, 45.778, 58.182, 71.191, 89.94],
    'Apply Real Time (s)': [8.581, 25.84, 51.931, 89.102, 136.595, 198.015, 268.835, 339.519, 436.424, 527.525],
    'Refresh Real Time (s)': [1.93, 3.622, 5.813, 8.317, 11.363, 15.706, 20.303, 23.75, 28.621, 34.141]
}

# Creating DataFrame
df = pd.DataFrame(data)

# Plotting
plt.figure(figsize=(10, 6))

plt.plot(df['Count'], df['Init Real Time (s)'], marker='o', label='Init Real Time')
plt.plot(df['Count'], df['Plan Real Time (s)'], marker='o', label='Plan Real Time')
plt.plot(df['Count'], df['Apply Real Time (s)'], marker='o', label='Apply Real Time')
plt.plot(df['Count'], df['Refresh Real Time (s)'], marker='o', label='Refresh Real Time')

plt.title('Terraform Execution Time with null_resource with output block')
plt.xlabel('Count')
plt.ylabel('Time (s)')
plt.legend()
plt.grid(True)
plt.xticks(df['Count'])

plt.tight_layout()
plt.show()
