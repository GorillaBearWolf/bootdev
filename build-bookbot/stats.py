#!/usr/bin/env python3


def count_words(text):
    words = text.split()
    return len(words)


def count_letters(text):
    lowered = text.lower()

    letter_dict = {}

    for i in lowered:
        if i in letter_dict:
            letter_dict[i] += 1
        else:
            letter_dict[i] = 1

    return letter_dict


def print_report(path, word_count, letter_count):
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print(f"----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print(f"----------- Character Count ----------")
    for i in sorted(letter_count, key=letter_count.get, reverse=True):
        if i.isalpha():
            print(f"{i}: {letter_count[i]}")
    print("============= END ===============")
