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

def sort_key(tupl):
    return tupl[1]


def main():
    with open("books/frankenstein.txt", "r") as file:
        file_content = file.read()
        print("--- Begin report of books/frankenstein.txt---")
        num_words = len(file_content.split())
        print(f"{num_words} words found in the document.")
        letter_hist = letter_histogram(file_content)
        items = list(letter_hist.items())
        items.sort(reverse=True, key=sort_key)
        for item in items:
            print(f"The '{item[0]}' character was found {item[1]} times")
        
        print("--- End report ---")



main()