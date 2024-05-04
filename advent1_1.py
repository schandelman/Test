with open("input1.txt") as f:
    data = []
    for line in f:
        data.append(line.strip())

total = 0
for text in data:
    number = ""
    for char in text:
        if char.isdigit():
            number += char
            break
    for char in reversed(text):
        if char.isdigit():
            number += char
            break
    total += int(number)

print(total)