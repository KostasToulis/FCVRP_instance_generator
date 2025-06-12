import matplotlib.pyplot as plt


def plot_solution_construction_method():
    y = [92.37, 90.26, 92.89, 93.42, 93.95, 93.42]
    x = ['Memory-based', 'Substitution-based', 'Equal probability', '75% Memory-based', '80% Memory-based', '90% Memory-based']

    # plt.bar(x, y, color='lightgray', edgecolor='black', width=0.7)
    plt.bar(x, y, color=['#ff6961', '#ffe066', '#ff9999', '#ffcc99', '#ffb347', '#ffae42'], edgecolor='black', width=0.7)
    plt.xlabel('Solution Construction Balance')
    plt.ylabel('Solved (%)')
    plt.ylim(89, 95)
    # plt.title('Comparison of Methods')
    plt.xticks(rotation=30, ha='right')
    plt.tight_layout()
    plt.show()

def plot_solution_population():
    y = [93.95, 95.53, 96.05, 95.76]
    x = ['10*K', '7*K', '5*K', '3*K']

    plt.bar(x, y, color='lightgray', edgecolor='black', width=0.7)
    plt.xlabel('poolSize')
    plt.ylabel('Solved (%)')
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
    y = [86.2, 92.7, 96.6, 96.1]
    x = ['0', '0.2', '0.33', '0.5']
    plt.bar(x, y, color=['#ff6961', '#ff9999', '#ffcc99' , '#ffe066'], edgecolor='black', width=0.7)
    plt.xlabel('g probability')
    plt.ylabel('Solved (%)')
    plt.ylim(85, 98)
    plt.xticks(x)
    plt.tight_layout()
    plt.show()

def plot_line_g():
    # In the g folder I have 4 txt files. Each line has two elements: the first is the solution cost (y-axis) and the second is the second (x-axis).
    # Create a line plot for each file. The lines should be in different colors on the same chart. Additionally, label each line with the file name.
    import os
    import numpy as np
    g_folder = 'g'
    files = os.listdir(g_folder)
    colors = ['#77dd77', '#84b6f4', '#cbaacb', '#f49ac2']
    plt.figure(figsize=(10, 6))
    for i, file in enumerate(files):
        if file.endswith('.txt'):
            data = np.loadtxt(os.path.join(g_folder, file), delimiter=',')
            x = data[:, 1].astype(int)  # second column as int
            y = data[:, 0].astype(int)  # first column as int  # first column
            plt.plot(x, y, label=file[:-4], color=colors[i % len(colors)])  # remove .txt from label
    plt.xlabel('Time (s)')
    plt.ylabel('Solution Cost')
    plt.title('Solution Cost Over Time')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


# plot_solution_construction_method()
# plot_solution_population()
# plot_chain_length()
# plot_g_probability()
plot_line_g()