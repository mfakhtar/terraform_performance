import pandas as pd
import matplotlib.pyplot as plt

# Provided data
data = {
    'Count': [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000],
    'Type': ['null_resource count'] * 10,
    'Init Real Time (s)': [0.839, 0.799, 0.779, 0.797, 1.131, 0.831, 0.818, 0.923, 1.548, 0.774],
    'Plan Real Time (s)': [0.784, 0.666, 0.823, 0.994, 1.215, 1.339, 1.583, 1.705, 2.131, 2.037],
    'Apply Real Time (s)': [3.682, 8.786, 15.54, 24.141, 34.597, 48.472, 63.639, 80.271, 99.122, 121.209],
    'Refresh Real Time (s)': [0.468, 0.893, 1.467, 2.145, 2.917, 3.869, 4.913, 6.08, 7.4, 8.953]
}

# Creating DataFrame
df = pd.DataFrame(data)

# Plotting
plt.figure(figsize=(10, 6))

plt.plot(df['Count'], df['Init Real Time (s)'], marker='o', label='Init Real Time')
plt.plot(df['Count'], df['Plan Real Time (s)'], marker='o', label='Plan Real Time')
plt.plot(df['Count'], df['Apply Real Time (s)'], marker='o', label='Apply Real Time')
plt.plot(df['Count'], df['Refresh Real Time (s)'], marker='o', label='Refresh Real Time')

plt.title('Terraform Execution Time with null_resource count')
plt.xlabel('Count')
plt.ylabel('Time (s)')
plt.legend()
plt.grid(True)
plt.xticks(df['Count'])

plt.tight_layout()
plt.show()