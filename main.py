def main():#
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_book_words(text)
    letters = get_book_letters(text)
    sorted = sort_on(letters)
    report(sorted, book_path, num_words)


def get_book_words(text):
    words = text.split()
    return len(words)
    
def get_book_text(path):
    with open(path) as f:
        return f.read().lower()
    
def get_book_letters(text):
    letter_dict = {}
    for letter in text:
        if letter.isalpha():  
            if letter in letter_dict:
                letter_dict[letter] += 1
            else:
                letter_dict[letter] = 1
    return letter_dict

def sort_on(dict):
    sorted_dict = sorted(dict.items(), key=lambda item: item[1], reverse=True)
    return sorted_dict

def report(dict, book_path, num_words):
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    for letter, count in dict:
        print(f"The '{letter}' character was found {count} times")
    
    print(f"--- End report ---")
        

main()