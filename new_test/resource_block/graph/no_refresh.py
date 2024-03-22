import pandas as pd
import matplotlib.pyplot as plt

# Provided data
data = {
    'Resource Count': [500, 1000, 1500, 2000, 2500, 3000],
    'Plan Real Time with Refresh (s)': [3.102, 4.943, 7.281, 9.71, 11.821, 14.485],
    'Apply Real Time with Refresh (s)': [15.231, 52.761, 114.965, 194.765, 297.419, 435.531],
    'Plan Real Time without Refresh (s)': [2.932, 4.591, 6.53, 8.792, 11.071, 13.538],
    'Apply Real Time without Refresh (s)': [15.04, 51.997, 113.156, 192.842, 297.157, 432.722]
}

# Creating DataFrame
df = pd.DataFrame(data)

# Plotting
plt.figure(figsize=(10, 6))

plt.plot(df['Resource Count'], df['Plan Real Time with Refresh (s)'], marker='o', label='Plan Real Time with Refresh')
plt.plot(df['Resource Count'], df['Apply Real Time with Refresh (s)'], marker='o', label='Apply Real Time with Refresh')
plt.plot(df['Resource Count'], df['Plan Real Time without Refresh (s)'], marker='o', label='Plan Real Time without Refresh')
plt.plot(df['Resource Count'], df['Apply Real Time without Refresh (s)'], marker='o', label='Apply Real Time without Refresh')

plt.title('Terraform Execution Time with null_resource block with refresh')
plt.xlabel('Resource Count')
plt.ylabel('Time (s)')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
