
import sys
from stats import wordcounter, char_counter, sorted_dict

def get_book_text(filepath):
    with open(filepath) as f:
        filecontents = f.read()
    return filecontents

def get_filepath():

    user_input = sys.argv

    if len(user_input) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    return user_input[1]

def main():
    
    filepath = get_filepath()
    num_words = wordcounter(get_book_text(filepath))

    list_out = sorted_dict(char_counter(get_book_text(filepath)))

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in list_out:
        print(f"{i["char"]}: {i["num"]}")



main()