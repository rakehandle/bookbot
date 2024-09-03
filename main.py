def main():
    book_path = "books/frankenstein.txt"
    book = get_text(book_path)
    wordCount = word_count(book)
    charCount = char_count(book)
    print(f"{wordCount} words found in this text")
    print(f"Character counts: \n{charCount}")


def get_text(book):
    with open(book) as f:
        return f.read()

def word_count(text):
        return len(text.split())

def char_count(text):
    characters = {}
    for c in text:
        lowercase = c.lower()
        if lowercase in characters:
            characters[lowercase]+= 1
        else:
            characters[lowercase]=1
    return characters

main()
