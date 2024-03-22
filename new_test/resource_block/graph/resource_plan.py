import pandas as pd
import matplotlib.pyplot as plt

# Provided data
data = {
    'Resource Block Count': [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000],
    'type': ['null_resource block'] * 10,
#    'Init Real Time (s)': [2.116, 0.86, 0.794, 0.85, 2.05, 1.984, 0.838, 0.921, 0.884, 0.887],
    'Plan Real Time (s)': [0.652, 0.951, 1.585, 1.673, 2.041, 2.467, 3.329, 3.398, 3.873, 4.326],
#    'Apply Real Time (s)': [5.35, 15.218, 30.6, 52.312, 79.075, 112.247, 152.3, 193.002, 241.61, 292.884],
    'Refresh Real Time (s)': [0.577, 1.01, 1.464, 1.926, 2.411, 2.914, 3.841, 4.056, 4.646, 5.202]
}

# Creating DataFrame
df = pd.DataFrame(data)

# Plotting
plt.figure(figsize=(10, 6))

#plt.plot(df['Resource Block Count'], df['Init Real Time (s)'], marker='o', label='Init Real Time')
plt.plot(df['Resource Block Count'], df['Plan Real Time (s)'], marker='o', label='Plan Real Time')
#plt.plot(df['Resource Block Count'], df['Apply Real Time (s)'], marker='o', label='Apply Real Time')
plt.plot(df['Resource Block Count'], df['Refresh Real Time (s)'], marker='o', label='Refresh Real Time')

plt.title('Terraform fresh Execution Time with null_resource block')
plt.xlabel('Resource Block Count')
plt.ylabel('Time (s)')
plt.legend()
plt.grid(True)
plt.xticks(df['Resource Block Count'])

plt.tight_layout()
plt.show()
