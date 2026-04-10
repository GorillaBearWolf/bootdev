BOOK_PATH = "books/frankenstein.txt"

with open(BOOK_PATH) as file:
    book_text = file.read()

words = book_text.split()

lowered = book_text.lower()

letter_dict = {}

for i in lowered:
    if i in letter_dict:
        letter_dict[i] += 1
    else:
        letter_dict[i] = 1

# Create and print formatted report
print(f"--- Report of {BOOK_PATH} ---", "\n")
print(len(words), "words found in the text", "\n")
for i in sorted(letter_dict, key=letter_dict.get, reverse=True):
    if i.isalpha():
        print(f"The '{i}' character was found {letter_dict[i]} times")
print("\n", "--- End of report ---")
