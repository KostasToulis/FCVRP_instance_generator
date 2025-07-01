import matplotlib.pyplot as plt


def plot_solution_construction_method():
    y = [92.37, 93.42, 93.95, 93.42, 92.89, 90.26]
    x = ['Memory', '90% Memory', '80% Memory', '75% Memory',  'Equal probability', 'Substitution']

    # plt.bar(x, y, color='lightgray', edgecolor='black', width=0.7)
    plt.bar(x, y, color=['#ff6961', '#ffe066', '#ff9999', '#ffcc99', '#ffb347', '#ff5733'], edgecolor='black', width=0.7)
    plt.xlabel('Solution Reconstruction Balance', fontsize=18, labelpad=15)
    plt.ylabel('% of instances solved or improved', fontsize=18)
    plt.ylim(89, 95)
    # plt.title('Comparison of Methods')
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.tight_layout(pad=0.2)
    plt.show()

def plot_solution_population():
    y = [93.95, 95.53, 96.05, 95.76]
    x = ['10*K', '7*K', '5*K', '3*K']

    plt.bar(x, y, color='lightgray', edgecolor='black', width=0.7)
    plt.xlabel('poolSize')
    plt.ylabel('% of instances solved or improved', fontsize=18)
    plt.ylim(92, 97)
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
    y = [86.2, 92.7, 96.6, 96.1, 91.1]
    x = ['0', '0.2', '0.33', '0.5', '1']
    plt.bar(x, y, color=['#ff6961', '#ff9999', '#ffcc99', '#ffe066', 'orange'], edgecolor='black', width=0.7)
    plt.xlabel('g', fontsize=16)
    plt.ylabel('% of instances solved or improved', fontsize=18)
    plt.ylim(75, 100)
    plt.xticks(x, fontsize=16)
    plt.yticks(fontsize=16)
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


# plot_solution_construction_method()
# plot_solution_population()
# plot_chain_length()
plot_g_probability()
# plot_line_g()