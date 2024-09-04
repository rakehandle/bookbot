def main():
    book_path = "books/frankenstein.txt"
    book = get_text(book_path)
    wordCount = word_count(book)
    charCount = char_count(book)
    print(create_Report(book_path, wordCount, charCount))

def get_text(book):
    with open(book) as f:
        return f.read()

def word_count(text):
        return len(text.split())

def char_count(text):
    characters = {}
    for c in text:
        lowercase = c.lower()
        if c.isalpha() == False:
            continue
        elif lowercase in characters:
            characters[lowercase]+= 1
        else:
            characters[lowercase]=1
    sorted = sort_Chars(characters)
    return sorted

def sort_Chars(counts):
    char_List = []
    for c in counts:
        new_Dict={}
        new_Dict["name"]=c
        new_Dict["count"]= counts[c]
        char_List.append(new_Dict)
    char_List.sort(reverse=True, key=sort_on)
    return char_List

def sort_on(dict):
    return dict["count"]

def create_Report(text, words, chars):
    report = (f"--- Begin report of {text} ---\n {words} words found in the document\n\n")
    for i in chars:
        report += f"The '{i["name"]}' character was found {i["count"]} times\n"
    report += "--- End Report ---"
    return report

main()
