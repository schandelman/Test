with open("input2.txt") as f:
    total = 0
    for line in f:
        failed = False
        data = line.split()
        game_num = int(data[1][:-1])
        for thing1, thing2 in zip(data[2:], data[3:]):
            if 'red' in thing2:
                if int(thing1) > 12:
                    failed = True
                    break
            if 'green' in thing2:
                if int(thing1) > 13:
                    failed = True
                    break
            if 'blue' in thing2:
                if int(thing1) > 14:
                    failed = True
                    break
        if not failed:
            total += game_num
    print(total)