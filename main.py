import sys
from stats import get_num_words
from stats import get_char_count
from stats import chars_dict_to_sorted_list
def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    book_text = get_book_text(path)
    num_words = get_num_words(book_text)
    char_counts = get_char_count(book_text)

    chars_sorted = chars_dict_to_sorted_list(char_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
          
    for char_dict in chars_sorted:
        char = char_dict["char"]
        count = char_dict["count"]
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")
        
main()


