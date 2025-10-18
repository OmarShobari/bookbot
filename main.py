from stats import count_words, count_characters

def get_book_text(path):
    with open(path) as file:
        return file.read()



def main():
    book_path = "./books/frankenstein.txt"
    book_text = get_book_text(book_path)
    num_words = count_words(book_text)
    char_count = count_characters(book_text)
    print(f"Found {num_words} total words")
    print(char_count)
    


main()
