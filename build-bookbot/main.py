#!/usr/bin/env python3

import sys
from stats import count_words, count_letters, print_report


def get_book_text(path):
    with open(path) as f:
        book_text = f.read()
    return book_text


def main():
    if len(sys.argv) != 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    BOOK_PATH = sys.argv[1]
    text = get_book_text(BOOK_PATH)
    word_count = count_words(text)
    letter_count = count_letters(text)
    print_report(BOOK_PATH, word_count, letter_count)


if __name__ == "__main__":
    main()
