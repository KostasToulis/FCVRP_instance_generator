import numpy as np
from sklearn.manifold import MDS

class Model:
    def __init__(self):
        self.num_nodes = 0
        self.num_fam = 0
        self.num_req = 0
        self.capacity = 0
        self.vehicles = 0
        self.depot = None
        self.fam_members = []
        self.fam_req = []
        self.fam_dem = []
        self.cost_matrix = []
        self.nodes = None
        self.customers = None
        self.families = None
        self.solution = None


class Node:
    def __init__(self, idd, fam, costs, dem=0):
        self.ID = idd
        self.isRouted = False
        self.isDepot = False
        self.family = fam
        self.costs = costs
        self.demand = dem
        self.isTabuTillIterator = -1
        self.route = None
        self.x = 0
        self.y = 0


class Route:
    def __init__(self, idd, cap):
        self.id = idd
        self.sequenceOfNodes = []
        self.demand = 0
        self.cost = 0
        self.capacity = cap

    def update_demand(self):
        demand = 0
        for node in self.sequenceOfNodes:
            demand += node.demand
        self.demand = demand

    def update_cost(self):
        cost = 0
        for i in range(1, len(self.sequenceOfNodes)):
            cost += self.sequenceOfNodes[i].costs[self.sequenceOfNodes[i-1].id]
        self.cost = cost


class Family:
    def __init__(self, idd, nodes, dem, required):
        self.id = idd
        self.nodes = nodes
        self.demand = dem
        self.required = required


class Solution:
    def __init__(self):
        self.cost = 0.0
        self.routes = []
        self.sequenceOfNodes = []


def load_model(file_name):
    model = Model()
    all_nodes = []
    all_lines = list(open(file_name, "r"))

    line_counter = 0

    # 1st line
    ln = all_lines[line_counter]
    no_spaces = ln.split()

    model.num_nodes = int(no_spaces[0])
    model.num_fam = int(no_spaces[1])
    model.num_req = int(no_spaces[2])
    model.capacity = int(no_spaces[3])
    model.vehicles = int(no_spaces[4])

    # 2nd line
    line_counter += 1
    ln = all_lines[line_counter]
    no_spaces = list(map(int, ln.split()))
    model.fam_members = no_spaces

    # 3rd line
    line_counter += 1
    ln = all_lines[line_counter]
    no_spaces = list(map(int, ln.split()))
    model.fam_req = no_spaces

    # 4th line
    line_counter += 1
    ln = all_lines[line_counter]
    no_spaces = list(map(int, ln.split()))
    model.fam_dem = no_spaces

    # 5th - end of file
    cost_matrix = []
    for i in range(model.num_nodes+1):
        line_counter += 1
        ln = all_lines[line_counter]
        no_spaces = list(map(int, ln.split()))
        cost_matrix.append(no_spaces)

    model.cost_matrix = cost_matrix
    model = create_nodes_families(model)
    model = compute_cartesian_coordinates(model)
    return model


def find_position(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < target:#+1:
            left = mid + 1
        else:
            right = mid - 1
    return left if left < len(arr) else -1


def create_nodes_families(model):
    families = []
    nodes = []
    for i in range(len(model.fam_members)):
        family = Family(i, [], model.fam_dem[i], model.fam_req[i])
        families.append(family)

    fam_index = []
    c = 0
    for i in model.fam_members:
        fam_index.append(i + c)
        c = i

    for i in range(len(model.cost_matrix)):
        if i == 0:
            node = Node(i, None, model.cost_matrix[i], None)
            node.isDepot = True
            model.depot = node
            nodes.append(node)
            continue
        family = find_position(fam_index, i)
        node = Node(i, family, model.cost_matrix[i], families[family].demand)
        nodes.append(node)

    for node in nodes:
        if node.family:
            families[node.family].nodes.append(node)

    for family in families:
        for node in family.nodes:
            node.family = family.id

    model.families = families
    model.nodes = nodes
    model.customers = nodes[1:]
    return model


def compute_cartesian_coordinates(model):
    cost_matrix = np.array(model.cost_matrix)
    mds = MDS(n_components=2, dissimilarity='precomputed')
    transformed_coords = mds.fit_transform(cost_matrix)

    for i, node in enumerate(model.nodes):
        node.x, node.y = transformed_coords[i]

    return model