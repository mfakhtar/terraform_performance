import matplotlib.pyplot as plt
import pandas as pd

# Data
data = {
    'Folder Name': ['resource_block', 'resource_block', 'resource_block', 'resource_block',
                    'count', 'count', 'count', 'count',
                    'for_each', 'for_each', 'for_each', 'for_each'],
    'Terraform Version': ['1.0.0', '0.12.6', '1.5.0', '1.7.0',
                          '1.0.0', '0.12.6', '1.5.0', '1.7.0',
                          '1.0.0', '0.12.6', '1.5.0', '1.7.0'],
    'Init Real Time (s)': [0.611, 4.921, 0.25, 0.667,
                            0.626, 1.128, 0.89, 0.25,
                            1.601, 3.163, 0.186, 0.204],
    'Plan Real Time (s)': [3.881, 5.284, 1.737, 1.792,
                            2.354, 2.697, 1.111, 0.933,
                            7.768, 8.009, 4.604, 4.726],
    'Apply Real Time (s)': [73.852, 65.856, 46.402, 43.13,
                             31.714, 30.648, 20.702, 19.416,
                             41.505, 44.065, 27.157, 25.979],
    'Refresh Real Time (s)': [4.711, 3.598, 1.71, 1.71,
                               4.402, 3.022, 1.779, 1.785,
                               8.66, 7.198, 4.687, 4.714]
}

# Create DataFrame
df = pd.DataFrame(data)

# Plot
fig, axs = plt.subplots(1, 4, figsize=(20, 5), sharey=True)

for i, command in enumerate(['Init', 'Plan', 'Apply', 'Refresh']):
    df.pivot(index='Terraform Version', columns='Folder Name', values=f'{command} Real Time (s)').plot(kind='bar', ax=axs[i], legend=True)
    axs[i].set_title(f'{command} Time (s)')
    axs[i].set_ylabel('Time (s)')
    axs[i].set_xlabel('Terraform Version')
    axs[i].grid(axis='y')

plt.tight_layout()
plt.show()
