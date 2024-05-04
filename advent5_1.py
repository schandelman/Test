def get_next(seed, mapping):
    for row in mapping:
        destination_start, source_start, length = row
        if seed >= source_start and seed <= source_start + length - 1:
            difference = seed - source_start
            return destination_start + difference
    return seed

mappings = []

with open("input5.txt") as f:
    seeds = [int(x) for x in f.readline().split()[1:]]
    f.readline()
    for i in range(7):
        next_mapping = []
        f.readline()
        next_line = f.readline().strip()
        while next_line != "":
            next_mapping.append([int(x) for x in next_line.split()])
            next_line = f.readline().strip()
        mappings.append(next_mapping)

locations = []
for seed in seeds:
    for mapping in mappings:
        seed = get_next(seed, mapping)
    locations.append(seed)

print(min(locations))