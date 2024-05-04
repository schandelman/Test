def contiguous_groups(data):
    current_size = 0
    in_group = False
    groups = []
    for cell in data:
        if not in_group:
            if cell == "#":
                current_size = 1
                in_group = True
        else:
            if cell == "#":
                current_size += 1
            else:
                groups.append(current_size)
                current_size = 0
                in_group = False
    if in_group:
        groups.append(current_size)
    return groups

def get_all_possibilities(data, string):
    if data == "":
        answers.append(string)
    elif data[0] == "?":
        get_all_possibilities(data[1:], string + ".")
        get_all_possibilities(data[1:], string + "#")
    else:
        get_all_possibilities(data[1:], string + data[0])

counter = 0
with open("input12.txt") as f:
    for line in f:
        data, groups = line.strip().split()
        groups = [int(x) for x in groups.split(",")]
        answers = []
        get_all_possibilities(data, "")
        for poss in answers:
            if contiguous_groups(poss) == groups:
                counter += 1

print(counter)

