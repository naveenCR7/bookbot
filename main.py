import sys
from stats import get_num_words, get_char_counts, sort_char_counts

def get_book_text(path_to_file):
    with open(path_to_file, encoding='utf-8') as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    text = get_book_text(path)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")

    num_words = get_num_words(text)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    char_counts = get_char_counts(text)
    sorted_chars = sort_char_counts(char_counts)

    for item in sorted_chars:
        print(f"{item['char']}: {item['count']}")

    print("============= END ===============")

main()
