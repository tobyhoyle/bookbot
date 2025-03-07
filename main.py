from stats import get_num_words, get_char_count, sort_chars
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_count = get_char_count(text)
    char_count = dict(sorted(char_count.items(), key=lambda item: item[1], reverse=True))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")  
    print("----------- Word Count ----------")
    print(f"{num_words}")
    print("--------- Character Count -------")
    for c in char_count:
        if c.isalpha():
            print(f"{c}: {char_count[c]}")
    print("============= END ===============")
    
if len(sys.argv) <= 1:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

main()