import os
import re

# directory = 'FCVRP-Best Solutions'
directory = 'newInstances-best'

for filename in os.listdir(directory):
    if filename.endswith('.txt'):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r') as f:
            lines = [line.rstrip('\n') for line in f]

        # Find all solution blocks
        solutions = []
        i = 0
        while i < len(lines):
            if lines[i].startswith('Cost:'):
                cost = float(re.findall(r'Cost:\s*([0-9.]+)', lines[i])[0])
                # Infer number of routes from the first solution
                if not solutions:
                    num_routes = 0
                    j = i + 1
                    while j < len(lines) and not lines[j].startswith('Cost:'):
                        num_routes += 1
                        j += 1
                routes = lines[i+1:i+1+num_routes]
                solutions.append((cost, [lines[i]] + routes))
                i += 1 + num_routes
            else:
                i += 1

        # Find the best solution
        if solutions:
            best = min(solutions, key=lambda x: x[0])
            with open(filepath, 'w') as f:
                for line in best[1]:
                    f.write(line + '\n')