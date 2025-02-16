# print("hello world")
def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    word_count = len(text.split())
    letter_counts = count_chars(text)

    #Header for the output
    print("-----Begin letter count report-----")

    print(f"There is a total word count of {word_count}")
    print()

    # Sort the dictionary by count
    sorted_letter_counts = sorted(letter_counts.items())

    #loop through the sorted list and print the key and value
    for letter, count in sorted_letter_counts:
        print(f"The '{letter}' was found {count} times.")

    #Footer for the output
    print()
    print("-----End letter count report-----")
 


def get_text(book_path):
    with open(book_path) as f:
        text = f.read()
    return text
    
    
    
def count_chars(text):
    letter_counts = {}
    for letter in text:
        if letter.isalpha():
            letter_string = letter.lower()
            if letter_string in letter_counts:
                letter_counts[letter_string] += 1
            else:
                letter_counts[letter_string] = 1
    #print(sorted_letter_counts)
    return (letter_counts)
       
main()
