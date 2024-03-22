import matplotlib.pyplot as plt

data = {
    "resource_block": {
        "1.0.0": {"Init": 0.611, "Plan": 3.881, "Apply": 73.852, "Refresh": 4.711},
        "0.12.6": {"Init": 4.921, "Plan": 5.284, "Apply": 65.856, "Refresh": 3.598},
        "1.5.0": {"Init": 0.25, "Plan": 1.737, "Apply": 46.402, "Refresh": 1.71},
        "1.7.0": {"Init": 0.667, "Plan": 1.792, "Apply": 43.13, "Refresh": 1.71},
    },
    "count": {
        "1.0.0": {"Init": 0.626, "Plan": 2.354, "Apply": 31.714, "Refresh": 4.402},
        "0.12.6": {"Init": 1.128, "Plan": 2.697, "Apply": 30.648, "Refresh": 3.022},
        "1.5.0": {"Init": 0.89, "Plan": 1.111, "Apply": 20.702, "Refresh": 1.779},
        "1.7.0": {"Init": 0.25, "Plan": 0.933, "Apply": 19.416, "Refresh": 1.785},
    },
    "for_each": {
        "1.0.0": {"Init": 1.601, "Plan": 7.768, "Apply": 41.505, "Refresh": 8.66},
        "0.12.6": {"Init": 3.163, "Plan": 8.009, "Apply": 44.065, "Refresh": 7.198},
        "1.5.0": {"Init": 0.186, "Plan": 4.604, "Apply": 27.157, "Refresh": 4.687},
        "1.7.0": {"Init": 0.204, "Plan": 4.726, "Apply": 25.979, "Refresh": 4.714},
    },
}

versions = ["1.0.0", "0.12.6", "1.5.0", "1.7.0"]

# Plotting for each folder
for folder, folder_data in data.items():
    plt.figure(figsize=(10, 6))
    for version in versions:
        init_times = [folder_data[version]["Init"]]
        plan_times = [folder_data[version]["Plan"]]
        apply_times = [folder_data[version]["Apply"]]
        refresh_times = [folder_data[version]["Refresh"]]
        plt.plot(init_times, label=f"Init - {version}")
        plt.plot(plan_times, label=f"Plan - {version}")
        plt.plot(apply_times, label=f"Apply - {version}")
        plt.plot(refresh_times, label=f"Refresh - {version}")

    plt.title(f"{folder.capitalize()} Execution Times")
    plt.xlabel("Iterations")
    plt.ylabel("Time (s)")
    plt.xticks(range(len(versions)), versions)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
