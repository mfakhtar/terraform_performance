import pandas as pd
import matplotlib.pyplot as plt

# Provided data
data = {
    'Count': [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000],
    'Type': ['null_resource with output block (count)'] * 10,
    'Init Real Time (s)': [1.051, 1.098, 0.99, 0.997, 1.052, 1.015, 6.156, 0.994, 1.001, 6.03],
    'Plan Real Time (s)': [1.731, 2.157, 2.589, 3.282, 3.567, 3.989, 4.462, 4.942, 5.717, 6.023],
    'Apply Real Time (s)': [4.736, 11.337, 20.378, 31.264, 45.91, 62.802, 81.725, 104.179, 130.33, 159.832],
    'Refresh Real Time (s)': [1.339, 2.192, 3.267, 4.629, 5.898, 7.539, 9.475, 11.624, 13.719, 16.271]
}

# Creating DataFrame
df = pd.DataFrame(data)

# Plotting
plt.figure(figsize=(10, 6))

plt.plot(df['Count'], df['Init Real Time (s)'], marker='o', label='Init Real Time')
plt.plot(df['Count'], df['Plan Real Time (s)'], marker='o', label='Plan Real Time')
plt.plot(df['Count'], df['Apply Real Time (s)'], marker='o', label='Apply Real Time')
plt.plot(df['Count'], df['Refresh Real Time (s)'], marker='o', label='Refresh Real Time')

plt.title('Terraform Execution Time with null_resource with output block (count)')
plt.xlabel('Count')
plt.ylabel('Time (s)')
plt.legend()
plt.grid(True)
plt.xticks(df['Count'])

plt.tight_layout()
plt.show()
