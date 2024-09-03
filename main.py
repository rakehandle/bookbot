def main():
    book_path = "books/frankenstein.txt"
    book = get_text(book_path)
    wordCount = word_count(book)
    print(f"{wordCount} words found in this text")


def get_text(book):
    with open(book) as f:
        return f.read()

def word_count(text):
        return len(text.split())

main()
