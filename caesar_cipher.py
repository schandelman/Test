def caesar_cipher(word, number):
    answer = ""
    for letter in word:
        answer += rotate_letter(letter, number)
    return answer

def rotate_letter(letter, number):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    location= alphabet.find(letter)
    location = (location + number) % 26
    return alphabet[location]




words = []

with open("2of12.txt") as f:
    for word in f:
        word = word.strip()
        if len(word) == 4:
            words.append(word)

words = set(words)


answers = {}
for word in words:
    for i in range(1,26):
        new_word = caesar_cipher(word, i)
        if new_word in words:
            if i in answers:
                answers[i].append((word, new_word))
            else:
                answers[i] = [(word, new_word)]

print(answers[20])


