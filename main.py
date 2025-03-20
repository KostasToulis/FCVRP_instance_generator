import random
import itertools
from best_fit import solve_bpp

random.seed(0)

class Family:

    def __init__(self, i):
        self.id = i
        self.nodes = []
        self.demand = random.randint(5, 30)
        self.required = 0

    def update_requirement(self, vp):
        ref = random.randint(1, len(self.nodes))
        low = random.randint(1, ref)
        high = random.randint(ref, len(self.nodes))
        ran = random.randint(low, high)

        self.required = {
            1: ref,
            2: low,
            3: high,
            4: ran
        }.get(vp, self.required)

    def add_node(self, node):
        self.nodes.append(node)



class Node:

    def __init__(self, i, fam):
        self.id = i
        self.x = random.randint(-100, 100)
        self.y = random.randint(-100, 100)
        self.family = fam
        self.demand = fam.demand if fam else 0
        self.costs = []


class Model:

    def __init__(self, nodes, families, num_req, vehicles, capacity, cost_matrix, name):
        self.num_nodes = len(nodes)
        self.num_fam = len(families)
        self.num_req = num_req
        self.vehicles = vehicles
        self.capacity = capacity
        self.nodes = nodes
        self.families = families
        self.cost_matrix = cost_matrix
        self.name = name


def output_model_to_file(model):
    with open (f"instances/{model.name}.txt", "w") as file:
        file.write(f"{model.num_nodes - 1} {model.num_fam} {model.num_req} {model.capacity} {model.vehicles}\n")
        for family in model.families:
            file.write(f"{len(family.nodes)} ")
        file.write("\n")
        for family in model.families:
            file.write(f"{family.required} ")
        file.write("\n")
        for family in model.families:
            file.write(f"{family.demand} ")
        file.write("\n")
        for node in model.nodes:
            file.write(" ".join(map(str, node.costs)) + "\n")

        file.close()


nodes_num = [150, 200, 300, 400]
fam_num_percent = [0.1, 0.3, 0.5]
visit_pattern = [1, 2, 3, 4]
symmetric = [0, 1]
capacity = [220, 250, 270, 300]

# permutations = list(itertools.product(nodes_num, fam_num_percent, visit_pattern, symmetric))
# print(f"Number of permutations: {len(permutations)}")
models = []

for n in nodes_num:
    for f in fam_num_percent:

        fam_num = (int)(n * f)
        families = [Family(i) for i in range(fam_num)]
        depot = Node(0, None)
        nodes = [depot]

        # Each family gets at least 1 node
        for i in range(fam_num):
            node = Node(i + 1, families[i])
            families[i].add_node(node)
            nodes.append(node)

        # The rest are randomly distributed
        for i in range(fam_num + 1, n + 1):
            family = random.choice(families)
            node = Node(i, family)
            family.add_node(node)
            nodes.append(node)

        c = 1

        # Reset node ids
        for family in families:
            for node in family.nodes:
                node.id = c
                c+=1

        nodes.sort(key=lambda x: x.id)

        for s in symmetric:
            if s==1:
                # Symmetric costs based on eucleidian distance
                for i in range(n + 1):
                    for j in range(i + 1, n + 1):
                        cost = round(((nodes[i].x - nodes[j].x) ** 2 + (nodes[i].y - nodes[j].y) ** 2) ** 0.5 / 2)
                        nodes[i].costs[j] = cost
                        nodes[j].costs[i] = cost

            else:
                for i in range(n + 1):
                    for j in range(n + 1):
                        if i == j:
                            nodes[i].costs.append(1000000)
                        else:
                            nodes[i].costs.append(random.randint(5, 85))

            costs = [node.costs for node in nodes]

            q = random.choice(capacity)

            for v in visit_pattern:
                n_req = 0
                for family in families:
                    family.update_requirement(v)
                    n_req += family.required

                vehicles = solve_bpp(families, q)

                a = "P" if s else "A"

                name = f"fcvrp_{a}{n+1}_{fam_num}_{vehicles}_{v}"

                model = Model(nodes, families, n_req, vehicles, q, costs, name)

                print(len(nodes))
                print(name)

                models.append(model)

                output_model_to_file(model)
