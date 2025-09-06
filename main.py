from stats import get_num_words, get_character_count, sort_dictionary
import sys

def get_book_text(file_input):
    # open file
    with open(file_input) as f:
        # read text into variable
        file_text = f.read()
    # return text
    return file_text

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    # input_text = "books/frankenstein.txt"
    input_text = sys.argv[1]
    text = get_book_text(input_text)
    
    num_words = get_num_words(text)
    # print(f"{num_words} words found in the document")
    
    num_characters = get_character_count(text)
    # print(num_characters)

    sorted_count = sort_dictionary(num_characters)

    print(f"""============ BOOKBOT ============
Analyxing book found at {input_text}...
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------""")
    for item in sorted_count:
        print(f"{item["char"]}: {item["num"]}")

if __name__ == "__main__":
    main()