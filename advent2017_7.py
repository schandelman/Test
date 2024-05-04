data = {}

with open("input2017_7.txt") as f:
    for line in f:
        line = line.strip().split()
        parent = line[0]
        weight = line[1][1:-1]
        if parent in data:
            data[parent][1] = int(weight)
        else:
            data[parent] = [None, int(weight)]
        if len(line) > 2:
            for child in line[3:]:
                child = child.strip(",")
                if child in data:
                    data[child][0] = parent
                else:
                    data[child] = [parent, 0]


current = 'vpryah'
while data[current][0] != None:
    current = data[current][0]

print(data)
