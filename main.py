path_to_file = "books/frankenstein.txt"

file_contents = None
with open(path_to_file) as f:
    file_contents = f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    text = text.lower()
    letters = {}
    for letter in text:
        try:
            letters[letter] = letters[letter] + 1
        except KeyError:
            letters[letter] = 1
    return letters


print(f"--- Begin report of {path_to_file} ---")
print(f"{count_words(file_contents)} words found in the document")
print("")
letters = list(count_letters(file_contents).items())
letters.sort()
for letter in letters:
    if letter[0].isalpha():
        print(f"The '{letter[0]}' character was found {letter[1]} times")
print("--- End report ---")
