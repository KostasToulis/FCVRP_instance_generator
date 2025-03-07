class Bin:
    def __init__(self, i, q):
        self.id = i
        self.capacity = q
        self.load = 0
        self.items = []




def solve_bpp(families, capacity):
    bins = []
    families.sort(key=lambda x: x.demand, reverse=True)
    for family in families:
        c = 0
        for node in family.nodes:
            best_bin = None
            best_fit = float('inf')
            for bin in bins:
                if bin.load + node.demand <= bin.capacity:
                    if bin.capacity - (bin.load + node.demand) < best_fit:
                        best_fit = bin.capacity - (bin.load + node.demand)
                        best_bin = bin
            if best_bin is None:
                best_bin = Bin(len(bins), capacity)
                bins.append(best_bin)
            best_bin.load += node.demand
            best_bin.items.append(node)
            c+=1
            if c >= family.required:
                break

    return len(bins)