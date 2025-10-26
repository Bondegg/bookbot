from stats import book_word_count, book_character_count, sort_word_count
import sys

def get_book_text(filepath):
    with open(filepath) as book:
        return book.read()
    
def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    word_count = book_word_count(book_text)
    character_dict = book_character_count(book_text)
    character_count_sorted = sort_word_count(character_dict)
    print(f"Found {word_count} total words")
    
    for entry in character_count_sorted:
        char = entry["char"]
        num = entry["num"]

        if char.isalpha():
            print(f"{char}: {num}")
        else:
            continue
    

main()
