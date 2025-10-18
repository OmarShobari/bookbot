def get_book_text(path):
    with open(path) as file:
        return file.read()


def main():
    book_path = "./books/frankenstein.txt"
    book_text = get_book_text(book_path)
    print(book_text)

main()