with open("input2.txt") as f:
    total = 0
    for line in f:
        failed = False
        data = line.split()
        game_num = int(data[1][:-1])
        reds = []
        greens = []
        blues = []
        for thing1, thing2 in zip(data[2:], data[3:]):
            if 'red' in thing2:
                reds.append(int(thing1))
            if 'green' in thing2:
                greens.append(int(thing1))
            if 'blue' in thing2:
                blues.append(int(thing1))
        power = max(reds) * max(greens) * max(blues)
        total += power
    print(total)