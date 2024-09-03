def main():
    book_path = "books/frankenstein.txt"
    book = get_text(book_path)
    wordCount = word_count(book)
    charCount = char_count(book)
    report = create_Report(book_path, wordCount,charCount)
    print(report)

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

def create_Report(book, words, characters):
    report = f"--- Begin report of {book} ---\n{words} words found in {book}\n"
    for c in characters:
        if c != "'":
            report += f"The '{c}' character was found {characters[c]} times\n"
        else:
            print("if statement works")
            report += f"The \' character was found {characters[c]} times\n"
    return report

main()
