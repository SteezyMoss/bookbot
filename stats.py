import sys

def get_book_text():
    path = sys.argv[1]
    with open(path) as f:
        file = f.read()

    return file

def book_length():
    book = get_book_text()
    word_lst = book.split()
    num_of_words = len(word_lst)

    return f"Found {num_of_words} total words"

def letter_count():
    letter_dict = {}
    book = get_book_text().lower()

    for letter in book:
        if letter.isalpha():
            if letter not in letter_dict:
                letter_dict[letter] = 1
            else:
                letter_dict[letter] += 1

    return letter_dict


def sort_on(items):
    return items["num"]
# this function will take the letter_count dict and return a sorted list of dicts
# each list index will be a dictionary with a char: and a num: key as well as there respective values
def sort_dict():
    unsorted_dict = letter_count()
    sorted_lst = []
    for key in unsorted_dict:
        tmp_dict = {}
        tmp_dict["char"] = key
        tmp_dict["num"] = unsorted_dict[key]
        sorted_lst.append(tmp_dict)

    sorted_lst.sort(reverse=True, key=sort_on)

    return sorted_lst



