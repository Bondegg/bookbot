from stats import book_word_count, book_character_count, sort_word_count

def get_book_text(filepath):
    with open(filepath) as book:
        return book.read()
    
def main():
    book_path = "books/frankenstein.txt"
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
