import sys
from stats import book_length, sort_dict

def main():
    if len(sys.argv) == 2:
        print(book_length())
        sorted_dict = sort_dict()
        for dict in sorted_dict:
            print(f"{dict['char']}: {dict['num']}")
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


main()