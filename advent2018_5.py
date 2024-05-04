import copy

with open("input2018_5.txt") as f:
    data = [x for x in f.read().strip()]

alphabet = "abcdefghijklmnopqrstuvwxyz"

def remove_polymers(string):
    i = 0
    while i < len(string)-1:
        if string[i].lower() == string[i+1].lower() and (string[i].islower() != string[i+1].islower()):
            del string[i]
            del string[i]
            if i >= 2:
                i -= 2
            else:
                i = -1
        i += 1
    return len(string)

def remove_one(string, letter):
    new_string = []
    for c in string:
        if c.lower() != letter:
            new_string.append(c)
    return new_string

d = {}
for letter in alphabet:
    new_data = remove_one(data, letter)
    d[letter] = remove_polymers(new_data)

print(d[min(d, key = d.get)])