def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    book_word_count = count_words(book_text)
    list_of_chars_sorted = (dict_to_list_sorted(count_chars(book_text)))

    generate_report(book_path,book_word_count,list_of_chars_sorted)

def generate_report(path,word_count,list_sorted):
    print(f"--- Word and Character Count for {path} ---")
    print(f"This book has a total of {word_count} words.\n")

    list_sorted.sort(key=get_num,reverse=True)
    for dict in list_sorted:
        char = dict['name']
        count = dict['num']
        if char.isalpha():
            print(f"The character '{char}' appeared {count} times.")

#This function takes a dictionary and converts into a list of dictionaries that can utilize .sort().
def dict_to_list_sorted(dict):
    list = []
    for key in dict:
        value = dict[key]
        list.append({"name":key,"num":value})
    return list

def get_num(dict):
    return dict['num']

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