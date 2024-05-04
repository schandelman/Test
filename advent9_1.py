def get_differences(lst):
    return [item2 - item1 for item1, item2 in zip(lst, lst[1:])]

def go_deeper(lst):
    if all(x == 0 for x in lst):
        return 0
    else:
        return lst[-1] + go_deeper(get_differences(lst))

total = 0
with open("input9.txt") as f:
    for line in f:
        line = [int(x) for x in line.split()]
        total += go_deeper(line)

print(total)

