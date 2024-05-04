def determine_hand(pair):
    cards = {}
    hand = pair[0]
    print(hand)
    card_values = {'2':2, '3':3, '4':4, '5':5,
                   '6':6, '7':7, '8':8, '9':9,
                   'T':10, 'J':1, 'Q':12, 'K':13, 'A':14}
    for card in hand:
        if card in cards:
            cards[card] += 1
        else:
            cards[card] = 1

    if 'J' in cards:
        joker_num = cards['J']
        if joker_num == 5:
            return (7, 1, 1, 1, 1, 1)
        del cards['J']
        best_card = max(cards, key = cards.get)
        cards[best_card] += joker_num
    counts = list(cards.values())
    if 5 in counts:
        hand_value = 7
    elif 4 in counts:
        hand_value = 6
    elif 3 in counts and 2 in counts:
        hand_value = 5
    elif 3 in counts:
        hand_value = 4
    elif counts.count(2) == 2:
        hand_value = 3
    elif 2 in counts:
        hand_value= 2
    else:
        hand_value = 1
    rankings = (hand_value,)
    for card in hand:
        rankings += (card_values[card],)
    return rankings


hand_dict = {1: "High Card", 2: "One pair", 3:"Two pair", 4:"Three of a kind", 5:"Full house",
             6:"Four of a kind", 7:"Five of a kind"}

data = []
with open("input_7.txt") as f:
    for line in f.readlines():
        hand, bid = line.strip().split()
        bid = int(bid)
        data.append([hand, bid])

data = sorted(data, key=determine_hand)

total = 0
for i, element in enumerate(data):
    hand, bid = element
    total += (i+1) * bid

print(total)