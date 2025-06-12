from setup import *
import matplotlib.pyplot as plt


# def plot_solution(solution, model):
#     plt.figure(figsize=(10, 10))
#
#     # Create a color map for families
#     family_colors = {fam.id: plt.cm.tab20(i) for i, fam in enumerate(model.families)}
#
#     for route in solution.routes:
#         x_coords = [node.x for node in route.sequenceOfNodes]
#         y_coords = [node.y for node in route.sequenceOfNodes]
#
#         # Draw the route
#         plt.plot(x_coords, y_coords, marker='o', label=f'Route {route.id}',
#                  color=family_colors.get(route.sequenceOfNodes[0].family, 'black'))
#
#         # Annotate nodes with their IDs
#         for node in model.nodes:
#             plt.text(node.x, node.y, str(node.ID), fontsize=9, ha='right')
#
#     plt.title('Solution Routes')
#     plt.xlabel('X Coordinate')
#     plt.ylabel('Y Coordinate')
#     plt.grid()
#     plt.legend()
#     plt.show()

def plot_solution(solution, model):
    plt.figure(figsize=(10, 10), dpi=400)

    # Create a color map for families
    family_colors = {fam.id: plt.cm.tab20(i % 20) for i, fam in enumerate(model.families)}

    for route in solution.routes:
        x_coords = [node.x for node in route.sequenceOfNodes]
        y_coords = [node.y for node in route.sequenceOfNodes]

        # Draw the route
        plt.plot(x_coords, y_coords, color='gray', linestyle='--', zorder=1)

    # Draw each node as a circle, colored by family
    for node in model.nodes:
        color = family_colors.get(node.family, 'black')  # Default to black if no family
        plt.scatter(node.x, node.y, s=400, color=color, edgecolors='black', zorder=3)  # Increased size (s=200)
        plt.text(node.x, node.y, str(node.ID), fontsize=12, ha='center', va='center', color='white', zorder=4)

    # Create a custom legend for families
    legend_elements = [
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=color, markersize=10, label=f'$l_{{{fam}}}$')
        for fam, color in family_colors.items()
    ]
    plt.legend(handles=legend_elements, title="Families", loc='upper right')

    # plt.title('Solution Routes')
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.grid()
    plt.show()

model = load_model('fcvrp_P-n40-k5_4_3_1.txt')

sol = Solution()

i=0

with open('solution.txt', 'r') as file:
    for line in file:

        parts = line.strip().split('-')
        if len(parts) < 2:
            continue
        route_id = i
        sequence_of_nodes = []#list(model.nodes[map(int, parts[0:])])
        for node_id in parts:
            sequence_of_nodes.append(model.nodes[int(node_id)])
        # Create a new Route object and populate it.
        route = Route(route_id, model.capacity)
        route.sequenceOfNodes = sequence_of_nodes

        # Add the route to the solution.
        sol.routes.append(route)
        print(f"Route {route_id} with nodes: {[node.ID for node in route.sequenceOfNodes]}")
        i+=1

# I want to create a plot of the solution.
# Each node has an x and y coordinate.
# Each node has a family, which has a color.
# The plot should show the routes with lines connecting the nodes.
plot_solution(sol, model)