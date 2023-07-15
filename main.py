def letter_histogram(string):
    letter_histogram = {}
    string = string.lower()

    for char in string:
        if char.isalpha():
            if char not in letter_histogram:
                letter_histogram[char] = 1
            else:
                letter_histogram[char] += 1

    return letter_histogram

def invert_dict(dic):
    inverted_dict = {}
    for key in dic:
        value = dic[key]
        if value not in inverted_dict:
            inverted_dict[value] = [key]
        else:
            inverted_dict[value].append(key)
    
    return inverted_dict

def sort_dict(dic):
    sorted_dict = {}
    keys = list(dic.keys())
    keys.sort(reverse=True)
    for key in keys:
        sorted_dict[key] = dic[key]
    
    return sorted_dict


def main():
    with open("books/frankenstein.txt", "r") as file:
        file_content = file.read()
        print("--- Begin report of books/frankenstein.txt---")
        num_words = len(file_content.split())
        print(f"{num_words} words found in the document.")
        letter_hist = letter_histogram(file_content)
        sorted_letter_hist = sort_dict(invert_dict(letter_hist))

        for count in sorted_letter_hist:
            letters = sorted_letter_hist[count]
            for letter in letters:
                print(f"The '{letter}' character was found {count} times")
        
        print("--- End report ---")



main()