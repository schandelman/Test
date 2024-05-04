import math

node_map = {}
current = []

with open("input8.txt") as f:
    instructions = f.readline().strip()
    line = f.readline()
    for line in f:
        current_node, next_nodes = line.strip().split(" = ")
        left_node, right_node = next_nodes.split(", ")
        left_node = left_node[1:]
        right_node = right_node[:-1]
        node_map[current_node] = [left_node, right_node]
        if current_node.endswith("A"):
            current.append(current_node)

counters = []
for start in current:
    node = start
    counter = 0
    while not node.endswith("Z"):
        instruction_num = counter % len(instructions)
        instruction = instructions[instruction_num]
        if instruction == "L":
            node = node_map[node][0]
        else:
            node = node_map[node][1]
        counter += 1
    counters.append(counter)

print(math.lcm(*counters))
