import matplotlib.pyplot as plt


def plot_solution_construction_method():
    # y = [92.37, 93.42, 93.95, 93.42, 92.89, 90.26]
    # y = [90.26, 92.89, 93.42, 93.95, 93.42, 92.37]

    y = [93.75, 94.55, 94.01, 94.79, 95.05, 94.79, 94.27]

    x = ['0', '0.5', '0.6', '0.7', '0.8',  '0.9', '1']

    plt.grid(axis='y', linestyle='--', alpha=0.7, zorder=0)
    # plt.bar(x, y, color='lightgray', edgecolor='black', width=0.7)
    # plt.bar(x, y, color=['#ff6961', '#ffe066', '#ff9999', '#ffcc99', '#ffb347', '#ff5733'], edgecolor='black', width=0.7)
    plt.bar(x, y, color=['lightgray', 'lightgray', 'lightgray', 'lightgray', 'tab:blue', 'lightgray', 'lightgray'], edgecolor='black',
            width=0.7, zorder=3)
    for i, v in enumerate(y):
        plt.text(i, v + 0.2, f"{v:.2f}", ha='center', fontsize=22, fontfamily='serif')
    plt.xlabel('Probability of using the PSC strategy', fontsize=22, labelpad=15, fontfamily='serif')
    plt.ylabel('Percentage of Solutions Matched or Improved (%)', fontsize=20, labelpad=10, fontfamily='serif')
    plt.ylim(93, 96)
    # plt.title('Comparison of Methods')
    plt.xticks(fontsize=20, fontfamily='serif')
    plt.yticks(fontsize=20, fontfamily='serif')
    plt.tight_layout(pad=0.2)
    plt.show()

def plot_solution_population():
    y = [89.32, 90.89, 89.32, 88.54]
    x = ['3*K', '5*K', '7*K', '10*K']
    plt.grid(axis='y', linestyle='--', alpha=0.7, zorder=0)
    plt.bar(x, y, color='lightgray', edgecolor='black', width=0.7, zorder=3)
    plt.xlabel('poolSize', fontsize=18, labelpad=15, fontfamily='serif')
    plt.ylabel('Percentage of Solutions Matched (%)', fontsize=18, fontfamily='serif')
    plt.ylim(85, 92)
    # plt.title('Comparison of Methods')
    # plt.xticks(rotation=30, ha='right')
    plt.tight_layout()
    plt.show()

def plot_chain_length():
    y = [92.37, 92.63, 90.79]
    x = ['0.3-0.5', '0.5-0.7', '0.7-0.9']
    plt.bar(x, y, color='lightgray', edgecolor='black', width=0.7)
    plt.xlabel('Chain Length')
    plt.ylabel('Solved (%)')
    plt.ylim(90, 93)
    # plt.title('Comparison of Methods')
    # plt.xticks(rotation=30, ha='right')
    plt.tight_layout()
    plt.show()

def plot_g_probability():
    y = [82.81, 84.38, 86.20, 90.89, 90.62, 89.84, 88.28]
    x = ['0', '0.1', '0.2', '0.3', '0.4', '0.5', '1']
    # plt.bar(x, y, color=['#ff6961', '#ff9999', '#ffcc99', '#ffe066', 'orange'], edgecolor='black', width=0.7)

    plt.grid(axis='y', linestyle='--', alpha=0.7, zorder=0)

    plt.bar(x, y, color=['lightgray', 'lightgray', 'lightgray', 'skyblue', 'lightgray', 'lightgray', 'lightgray'], edgecolor='black', width=0.7, zorder=3)
    # Add the y value to each bar
    for i, v in enumerate(y):
        plt.text(i, v + 0.2, f"{v:.2f}", ha='center', fontsize=24, fontfamily='serif')
    plt.xlabel('Probability g', fontsize=20, labelpad=15, fontfamily='serif')


    plt.ylabel('Percentage of Solutions Matched (%)', fontsize=20, fontfamily='serif', labelpad=15)
    plt.ylim(80, 92)
    plt.xticks(x, fontsize=22, fontfamily='serif')
    plt.yticks(fontsize=20, fontfamily='serif')
    plt.show()


def plot_top_arcs():
    y = [90.62, 88.80, 90.89, 89.84, 87.76]
    x = ['1%', '2%', '3%', '4%', '5%']

    plt.grid(axis='y', linestyle='--', alpha=0.7, zorder=0)

    plt.bar(x, y, color=['lightgray', 'lightgray', 'skyblue', 'lightgray', 'lightgray'], edgecolor='black', width=0.7, zorder=3)
    for i, v in enumerate(y):
        plt.text(i, v + 0.2, f"{v:.2f}", ha='center', fontsize=24, fontfamily='serif')
    plt.xlabel('Percentage of solution arcs for penalization', fontsize=20, labelpad=15, fontfamily='serif')
    # plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.ylabel('Percentage of Solutions Matched (%)', fontsize=20, fontfamily='serif', labelpad=15)
    plt.ylim(85, 92)
    plt.xticks(x, fontsize=24, fontfamily='serif')
    plt.yticks(fontsize=22, fontfamily='serif')
    plt.tight_layout()
    plt.show()

def plot_line_g():
    import os
    import numpy as np
    g_folder = 'g'
    files = os.listdir(g_folder)
    colors = ['#f49ac2', 'orange', 'yellow', 'red' ]
    plt.figure(figsize=(10, 6))
    for i, file in enumerate(files):
        if file.endswith('.txt'):
            data = np.loadtxt(os.path.join(g_folder, file), delimiter=',')
            x = data[:, 1].astype(int)
            y = data[:, 0].astype(int)
            plt.plot(x, y, label=file[::-1].split('_', 1)[0][::-1].replace('.txt', ''), color=colors[i % len(colors)])
    plt.ylim(430, 470)
    plt.xlim(0, 400)
    plt.xlabel('Time (s)', fontsize=16)
    plt.ylabel('Solution Cost', fontsize=16)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    # plt.title('Solution Cost Over Time')
    plt.axhline(y=432, color='grey', linestyle='--', linewidth=1)
    plt.legend(fontsize=22)
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def plot_g_topArcs_heatmap():
    no_g = 87.76
    # results = [[90.62, 90.62, 90.36, 91.93, 90.62],
    #            [91.41, 91.41, 90.89, 91.15, 91.41],
    #            [92.19, 93.23, 93.23, 93.23, 93.49],
    #            [93.75, 94.27, 94.53, 95.05, 93.23],
    #            [94.53, 94.01, 94.27, 94.27, 92.45],
    #            [94.53, 91.15, 91.41, 90.62, 89.32]]
    import numpy as np
    import seaborn as sns

    results = np.array([
        [87.76, 87.76, 87.76, 87.76, 87.76, np.nan],
        [90.62, 90.62, 90.36, 91.93, 90.62, np.nan],
        [91.41, 91.41, 90.89, 91.15, 91.41, np.nan],
        [92.19, 93.23, 93.23, 93.23, 93.49, np.nan],
        [93.75, 94.27, 94.53, 95.05, 93.23, np.nan],
        [94.53, 94.01, 94.27, 94.27, 92.45, np.nan],
        [94.53, 91.15, 91.41, 90.62, 89.32, np.nan]
    ])

    plt.figure(figsize=(8, 6))
    sns.heatmap(
        results[:, :6], annot=True, fmt=".2f", cmap="Blues", cbar=True,
        yticklabels=[0, 0.1, 0.2, 0.3, 0.4, 0.5, 1],
        xticklabels=['1%', '2%', '3%', '4%', '5%'],
        annot_kws={"fontsize": 20, "fontfamily": "serif"}
    )
    plt.ylabel('Probability g', fontsize=20, fontfamily='serif', labelpad=15)
    plt.xlabel('topArcs Percentage', fontsize=20, fontfamily='serif', labelpad=15)
    plt.xticks(fontsize=20, fontfamily='serif')
    plt.yticks(fontsize=20, fontfamily='serif')
    plt.tight_layout()
    plt.show()

# plot_solution_construction_method()
# plot_solution_population()
# plot_chain_length()
# plot_g_probability()
# plot_top_arcs()
# plot_line_g()
plot_g_topArcs_heatmap()