def get_book_text(filepath):
    with open(filepath) as book:
        return book.read()

def book_word_count(book_text):
    words = book_text.split()
    return len(words)

def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    word_count = book_word_count(book_text)
    print(f"Found {word_count} total words")

main()
