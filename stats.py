def book_word_count(book_text):
    words = book_text.split()
    return len(words)

def book_character_count(book):
    character_count = {}

    for word in book:
        lower_word = word.lower()
        for letter in lower_word:
            if letter in character_count:
                character_count[letter] += 1
            
            elif letter not in character_count:
                character_count[letter] = 1
            
            else:
                continue

    return character_count

def sort_by(items):
    return items["num"]

def sort_word_count(characters_dict):
    list_to_sort = []
    for key, value in characters_dict.items():
        temp_dict = {"char": key, "num": value}
        list_to_sort.append(temp_dict)
    
    list_to_sort.sort(reverse=True, key=sort_by)

    return list_to_sort

    

