total = 0

with open("input4.txt") as f:
    for line in f:
        winning, my_numbers = line.strip().split(" | ")
        winning = winning.split()[2:]
        my_numbers = my_numbers.split()
        score = 0
        for number in winning:
            if number in my_numbers:
                if score == 0:
                    score = 1
                else:
                    score *= 2
        total += score

print(total)