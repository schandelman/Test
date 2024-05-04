cards = []

card_wins = {}
card_counts = {}

with open("input4.txt") as f:
    for line in f:
        winning, my_numbers = line.strip().split(" | ")
        winning = winning.split()[2:]
        my_numbers = my_numbers.split()
        cards.append([winning, my_numbers])

for i, card in enumerate(cards):
    score = 0
    winning, my_numbers = card
    for number in winning:
        if number in my_numbers:
            score += 1
    card_wins[i] = score
    card_counts[i] = 1


for i in card_counts:
    wins = card_wins[i]
    for j in range(i+1, i+1+wins):
        card_counts[j] += card_counts[i]

print(sum(card_counts.values()))
