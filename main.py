def main():
    book_path = "books/frankenstein.txt"
    file_contents = read_book(book_path)
    words = count_words(file_contents)
    list_of_dict = sort_dict(char_counter_dict(file_contents))
    list_of_dict.sort(reverse=True, key=sort_on)
    
    print("---------- REPORT -----------")
    print(f"{len(words)} words found in the document")
    print_alpha_count(list_of_dict)
    print("---------- END OF REPORT -----------")

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

def print_alpha_count(list):
    for i in list:
        print(f"The {i['name']} character was found {i['num']} times")
            #print(f"The '{i}' character was found {dict[i]} times")

def sort_dict(dict):
    sort_list = []
    for i in dict:
        if i.isalpha() == True:
            sort_list.append({"name": i, "num": dict[i]})
    return sort_list

def sort_on(dict):
    return dict["num"]


main()

