import matplotlib.pyplot as plt

# Data dictionary to store execution times
data = {
    'init': [],
    'plan': [
        (10, 1.071),
        (20, 1.068),
        (30, 1.073),
        (40, 1.042),
        (50, 1.192)
    ],
    'apply': [
        (10, 13.228),
        (20, 13.488),
        (30, 14.168),
        (40, 14.055),
        (50, 13.676)
    ],
    'refresh': [
        (10, 0.858),
        (20, 0.839),
        (30, 0.831),
        (40, 0.909),
        (50, 0.831)
    ]
}

# Plot all histograms in a single graph
plt.figure(figsize=(10, 6))
plt.title('Execution Times for Different Actions (1000 resources)')
plt.xlabel('Parallelism')
plt.ylabel('Time (s)')

colors = {'plan': 'blue', 'apply': 'green', 'refresh': 'orange'}

for action, action_data in data.items():
    if action_data:
        parallelisms, times = zip(*action_data)
        plt.plot(parallelisms, times, label=action, marker='o', color=colors.get(action))

plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
