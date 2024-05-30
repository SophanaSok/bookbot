def main():
    book_path = "books/frankenstein.txt"
    file_contents = read_book(book_path)
    words = count_words(file_contents)
    
    print(f"{len(words)} words found in the document")
    how_often_letter_appears(num_of_char(file_contents))

def read_book(book):
    with open(book) as f:
        return f.read()
     
def count_words(content):
    return content.split()

def num_of_char(words):
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

def how_often_letter_appears(dict):
    for i in dict:
        if i.isalpha() == True:
            print(f"The '{i}' character was found {dict[i]} times")



main()

