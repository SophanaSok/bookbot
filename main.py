def main():
    book_path = "books/frankenstein.txt"
    file_contents = read_book(book_path)
    words = count_words(file_contents)
    
    print(f"{len(words)} words found in the document")
    print_alpha_count(char_counter_dict(file_contents))
    print(char_counter_dict(file_contents))

def read_book(book):
    with open(book) as f:
        return f.read()
     
def count_words(content):
    return content.split()

def char_counter_dict(words):
    char_list = {}
    lowercase_words = words.lower()
    words_list = lowercase_words.split()
    for word in words_list:
        for char in word:
            if char not in char_list:
                char_list[char] = 1
            else: 
                char_list[char] += 1
    return char_list

def print_alpha_count(dict):
    for i in dict:
        if i.isalpha() == True:
            print(f"The '{i}' character was found {dict[i]} times")



main()

