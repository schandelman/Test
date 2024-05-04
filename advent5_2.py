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
while seeds != []:
    seed, seed_range = seeds[0], seeds[1]
    seeds = seeds[2:]
    for s in range(seed, seed+seed_range+1):
        for mapping in mappings:
            s = get_next(s, mapping)
        locations.append(s)

print(min(locations))