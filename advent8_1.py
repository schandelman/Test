node_map = {}

with open("input8.txt") as f:
    instructions = f.readline().strip()
    line = f.readline()
    for line in f:
        current_node, next_nodes = line.strip().split(" = ")
        left_node, right_node = next_nodes.split(", ")
        left_node = left_node[1:]
        right_node = right_node[:-1]
        node_map[current_node] = [left_node, right_node]

counter = 0
current = "AAA"
while current != "ZZZ":
    instruction_num = counter % len(instructions)
    instruction = instructions[instruction_num]
    if instruction == "L":
        current = node_map[current][0]
    else:
        current = node_map[current][1]
    counter += 1

print(counter)
