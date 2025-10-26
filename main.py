from stats import book_word_count

def get_book_text(filepath):
    with open(filepath) as book:
        return book.read()
    
def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    word_count = book_word_count(book_text)
    print(f"Found {word_count} total words")

main()
