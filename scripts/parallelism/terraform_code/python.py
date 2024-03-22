import matplotlib.pyplot as plt

# Data dictionary to store execution times
data = {
    'init': [],
    'plan': [
        (10, 0.953),
        (20, 0.677),
        (30, 0.684),
        (40, 0.695),
        (50, 0.687)
    ],
    'apply': [
        (10, 4.955),
        (20, 4.976),
        (30, 5.193),
        (40, 5.105),
        (50, 5.223)
    ],
    'refresh': [
        (10, 0.486),
        (20, 0.491),
        (30, 0.493),
        (40, 0.474),
        (50, 0.481)
    ]
}

# Plot all histograms in a single graph
plt.figure(figsize=(10, 6))
plt.title('Execution Times for Different Actions')
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
