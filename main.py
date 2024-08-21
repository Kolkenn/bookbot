def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(count_chars(text))

#Take a file path and uses the open() method to open it and the read() to display.
def get_book_text(path):
    with open(path) as f:
        return f.read()

#Takes a string and return the number of words in it.
def count_words(text):
    return len(text.split())

#Takes a string and returns number of times each character appears.
def count_chars(text):
    char_dict = {}
    #Make all letters lowercase for easy sorting.
    words_list_lower = (text.lower()).split()
    #Loops through words in the list.
    for words in words_list_lower:
        #Loop through each char to build dictionary.
        for char in words:
            if char not in char_dict:
                char_dict[char] = 1
            else:
                char_dict[char] += 1
    return char_dict

main()