# print("hello world")
def main():
    with open("books/frankenstein.txt") as f:
        text = f.read()
    
    words = text.split()
    word_count = len(words)

    print(f"There is a total word count of {word_count}")
    
    def count_chars(text):
        letter_counts = {}
        for letter in text:
            if letter.isalpha():
                letter_string = letter.lower()
                if letter_string in letter_counts:
                    letter_counts[letter_string] += 1
                else:
                    letter_counts[letter_string] = 1
        # Sort the dictionary by count
        sorted_letter_counts = sorted(letter_counts.items())

        #Header for the output
        print("-----Begin letter count report-----")

        #loop through the sorted list and print the key and value
        for letter, count in sorted_letter_counts:
            print(f"The '{letter}' was found {count} times.")

        #Footer for the output
        print("-----End letter count report-----")

        #print(sorted_letter_counts)
        return (letter_counts)
    
    
    count_chars(text)

main()
