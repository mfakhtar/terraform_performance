import pandas as pd
import matplotlib.pyplot as plt

# Provided data
data = {
    'Resource Count': [500, 1000, 1500, 2000, 2500, 3000],
    'Init Real Time (Before Update)': [2.116, 0.86, 0.794, 0.85, 2.05, 1.984],
    'Plan Real Time (Before Update)': [0.652, 0.951, 1.585, 1.673, 2.041, 2.467],
    'Apply Real Time (Before Update)': [5.35, 15.218, 50.6, 52.312, 79.075, 112.247],
    'Refresh Real Time (Before Update)': [0.577, 1.01, 1.464, 1.926, 2.411, 2.914],
    'Init Real Time (After Update)': [1.494, 1.273, 4.662, 4.469, 2.603, 1.828],
    'Plan Real Time (After Update)': [3.102, 4.943, 7.281, 9.71, 11.821, 14.485],
    'Apply Real Time (After Update)': [15.231, 52.761, 114.965, 194.765, 297.419, 435.531],
    'Refresh Real Time (After Update)': [2.659, 4.726, 7.037, 9.716, 12.392, 15.428]
}

# Creating DataFrame
df = pd.DataFrame(data)

# Plotting
plt.figure(figsize=(12, 8))

# Before Update
#plt.bar(df['Resource Count'] - 200, df['Init Real Time (Before Update)'], width=50, label='Init Real Time (Before Update)')
plt.bar(df['Resource Count'] - 170, df['Plan Real Time (Before Update)'], width=50, label='Plan Real Time (Before Update)')
plt.bar(df['Resource Count'] - 140, df['Apply Real Time (Before Update)'], width=50, label='Apply Real Time (Before Update)')
plt.bar(df['Resource Count'] - 110, df['Refresh Real Time (Before Update)'], width=50, label='Refresh Real Time (Before Update)')

# After Update
#plt.bar(df['Resource Count'] + 110, df['Init Real Time (After Update)'], width=50, label='Init Real Time (After Update)')
plt.bar(df['Resource Count'] + 140, df['Plan Real Time (After Update)'], width=50, label='Plan Real Time (After Update)')
plt.bar(df['Resource Count'] + 170, df['Apply Real Time (After Update)'], width=50, label='Apply Real Time (After Update)')
plt.bar(df['Resource Count'] + 200, df['Refresh Real Time (After Update)'], width=50, label='Refresh Real Time (After Update)')

plt.title('Terraform Execution Time with null_resource block Before and After Updating Resource Count')
plt.xlabel('Resource Count')
plt.ylabel('Time (s)')
plt.legend()
plt.grid(True)
plt.xticks(df['Resource Count'])

plt.tight_layout()
plt.show()
