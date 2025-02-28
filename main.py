# print("hello world")
from stats import get_num_words
import sys

#import system arguments
def get_args():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    return sys.argv[1]

def main():
    book_path = get_args()
    text = get_text(book_path)
    letter_counts = count_chars(text)
    print(f"{get_num_words(text)} words found in the document")
    print()

    #Header for the output
    print("-----Begin letter count report-----")

    # Sort the dictionary by count, converts to a list of tuples
    sorted_letter_counts = sorted(letter_counts.items())

    #loop through the sorted list and print the key and value
    for letter, count in sorted_letter_counts:
        print(f"The '{letter}' was found {count} times.")

    #Footer for the output
    print()
    print("-----End letter count report-----")
 

#Extract the text from the file
def get_text(book_path):
    with open(book_path) as f:
        text = f.read()
    return text
    
    
#Produce dict with charecter counts
def count_chars(text):
    letter_counts = {}
    for letter in text:
        #Check if the charecter is a letter
        if letter.isalpha():
            #convert the letter to lower case and count in dictionary
            letter_string = letter.lower()
            if letter_string in letter_counts:
                letter_counts[letter_string] += 1
            else:
                letter_counts[letter_string] = 1
    #print(sorted_letter_counts)
    return (letter_counts)
       
main()
