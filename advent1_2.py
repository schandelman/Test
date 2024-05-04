with open("input1.txt") as f:
    data = []
    for line in f:
        data.append(line.strip())
numbers  = {"one":1, "two":2, "three":3, "four":4,
            "five":5, "six":6, "seven":7, "eight":8, "nine":9}
total = 0
for text in data:
    number = 0
    found = False
    for i, letter in enumerate(text):
        for word in numbers:
            if text[i:].startswith(word):
                number += (numbers[word] * 10)
        if number > 0:
            break
        if text[i].isdigit():
            number += (int(text[i]) * 10)
            break
    for i in range(len(text)-1, -1, -1):
        for word in numbers:
            if text[i:].startswith(word):
                number += numbers[word]
                found = True
                break
        if found:
            break
        if text[i].isdigit():
            number += int(text[i])
            break
    total += number

print(total)