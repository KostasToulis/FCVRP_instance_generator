import matplotlib.pyplot as plt


def plot_solution_construction_method():
    y = [92.37, 90.26, 92.89, 93.42, 93.95, 93.42]
    x = ['Memory-based', 'Substitution-based', 'Equal probability', '75% Memory-based', '80% Memory-based', '90% Memory-based']

    plt.bar(x, y, color='lightgray', edgecolor='black', width=0.7)
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

plot_solution_construction_method()
# plot_solution_population()
# plot_chain_length()