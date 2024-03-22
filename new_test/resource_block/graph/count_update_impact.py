import pandas as pd
import matplotlib.pyplot as plt

# Provided data
data = {
    'Resource Count': [500, 1000, 1500, 2000, 2500, 3000],
    'Init Real Time (Before Update)': [0.839, 0.799, 0.779, 0.797, 1.131, 0.831],
    'Plan Real Time (Before Update)': [0.784, 0.666, 0.823, 0.994, 1.215, 1.339],
    'Apply Real Time (Before Update)': [3.682, 8.786, 15.54, 24.141, 34.597, 48.472],
    'Refresh Real Time (Before Update)': [0.468, 0.893, 1.467, 2.145, 2.917, 3.869],
    'Init Real Time (After Update)': [1.289, 1.344, 1.36, 4.646, 1.293, 4.284],
    'Plan Real Time (After Update)': [2.422, 3.687, 5.183, 6.847, 9.098, 10.928],
    'Apply Real Time (After Update)': [9.251, 27.427, 56.339, 97.686, 151.144, 214.35],
    'Refresh Real Time (After Update)': [2.349, 4.376, 7.352, 11.191, 15.538, 21.548]
}

# Creating DataFrame
df = pd.DataFrame(data)

# Plotting
plt.figure(figsize=(12, 8))

# Before Update
plt.bar(df['Resource Count'] - 200, df['Init Real Time (Before Update)'], width=30, label='Init Real Time (Before Update)')
plt.bar(df['Resource Count'] - 170, df['Plan Real Time (Before Update)'], width=30, label='Plan Real Time (Before Update)')
plt.bar(df['Resource Count'] - 140, df['Apply Real Time (Before Update)'], width=30, label='Apply Real Time (Before Update)')
plt.bar(df['Resource Count'] - 110, df['Refresh Real Time (Before Update)'], width=30, label='Refresh Real Time (Before Update)')

# After Update
plt.bar(df['Resource Count'] + 110, df['Init Real Time (After Update)'], width=30, label='Init Real Time (After Update)')
plt.bar(df['Resource Count'] + 140, df['Plan Real Time (After Update)'], width=30, label='Plan Real Time (After Update)')
plt.bar(df['Resource Count'] + 170, df['Apply Real Time (After Update)'], width=30, label='Apply Real Time (After Update)')
plt.bar(df['Resource Count'] + 200, df['Refresh Real Time (After Update)'], width=30, label='Refresh Real Time (After Update)')

plt.title('Terraform Execution Time with null_resource block Before and After Updating Resource Count using count argument')
plt.xlabel('Resource Count')
plt.ylabel('Time (s)')
plt.legend()
plt.grid(True)
plt.xticks(df['Resource Count'])

plt.tight_layout()
plt.show()
