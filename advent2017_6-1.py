with open("input2017_6.txt") as f:
    data = [int(x) for x in f.read().split("\t")]

seen = [data[:]]
def redistribute(data):
    largest = max(data)
    for i, num in enumerate(data):
        if num == largest:
            break
    data[i] = 0
    while largest > 0:
        i = (i + 1) % len(data)
        data[i] += 1
        largest -= 1
    return data

#counter = 0
while True:
    #counter += 1
    data = redistribute(data)
    if data in seen:
        break
    seen.append(data[:])

counter = 1
loop_start = data[:]
data = redistribute(data)
while data != loop_start:
    data = redistribute(data)
    counter += 1
print(counter)