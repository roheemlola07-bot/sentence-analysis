sentence = input("Enter a sentence ending with a point: ")

length = 0
words = 1
vowels = 0

for c in sentence:
    if c == '.':
        break

    length = length + 1

    if c == ' ':
        words = words + 1

    if c in "aeiouAEIOU":
        vowels = vowels + 1

    if length == 0:
    words = 0

print("Length:", length)
print("Words:", words)
print("Vowels:", vowels)