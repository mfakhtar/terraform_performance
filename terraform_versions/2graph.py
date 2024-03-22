import matplotlib.pyplot as plt

# Data
data = {
    'resource_block': {
        'terraform_version': ['1.0.0', '0.12.6', '1.5.0', '1.7.0'],
        'Init_Real_Time': [0.611, 4.921, 0.25, 0.667],
        'Plan_Real_Time': [3.881, 5.284, 1.737, 1.792],
        'Apply_Real_Time': [73.852, 65.856, 46.402, 43.13],
        'Refresh_Real_Time': [4.711, 3.598, 1.71, 1.71]
    },
    'count': {
        'terraform_version': ['1.0.0', '0.12.6', '1.5.0', '1.7.0'],
        'Init_Real_Time': [0.626, 1.128, 0.89, 0.25],
        'Plan_Real_Time': [2.354, 2.697, 1.111, 0.933],
        'Apply_Real_Time': [31.714, 30.648, 20.702, 19.416],
        'Refresh_Real_Time': [4.402, 3.022, 1.779, 1.785]
    },
    'for_each': {
        'terraform_version': ['1.0.0', '0.12.6', '1.5.0', '1.7.0'],
        'Init_Real_Time': [1.601, 3.163, 0.186, 0.204],
        'Plan_Real_Time': [7.768, 8.009, 4.604, 4.726],
        'Apply_Real_Time': [41.505, 44.065, 27.157, 25.979],
        'Refresh_Real_Time': [8.66, 7.198, 4.687, 4.714]
    }
}

# Plotting
categories = list(data.keys())
terraform_versions = data['resource_block']['terraform_version']
bar_width = 0.2
index = range(len(terraform_versions))

for i, category in enumerate(categories):
    plt.bar([x + i * bar_width for x in index], data[category]['Init_Real_Time'], width=bar_width, label=f'{category} - Init')
    plt.bar([x + i * bar_width for x in index], data[category]['Plan_Real_Time'], width=bar_width, label=f'{category} - Plan', bottom=data[category]['Init_Real_Time'])
    plt.bar([x + i * bar_width for x in index], data[category]['Apply_Real_Time'], width=bar_width, label=f'{category} - Apply', bottom=[sum(x) for x in zip(data[category]['Init_Real_Time'], data[category]['Plan_Real_Time'])])
    plt.bar([x + i * bar_width for x in index], data[category]['Refresh_Real_Time'], width=bar_width, label=f'{category} - Refresh', bottom=[sum(x) for x in zip(data[category]['Init_Real_Time'], data[category]['Plan_Real_Time'], data[category]['Apply_Real_Time'])])

plt.xlabel('Terraform Version')
plt.ylabel('Time (s)')
plt.title('Real Time by Terraform Version and Action')
plt.xticks([r + bar_width for r in range(len(terraform_versions))], terraform_versions)
plt.legend()
plt.tight_layout()
plt.show()
