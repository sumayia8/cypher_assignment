import sys

user_sentence = sys.stdin.read().upper()
cipher = ""
shift = int(sys.argv[1])
letter_count = 0
line_count = 0

for char in user_sentence:
    if char.isalpha():
        current_unicode = ord(char)
        cipher += chr((current_unicode - 65 + shift) % 26 + 65)
        letter_count += 1
        line_count += 1
    if letter_count == 5:
        cipher += " "
        letter_count = 0
    if line_count == 50:
        cipher += "\n"
        line_count = 0

print(cipher)