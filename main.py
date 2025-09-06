from stats import get_num_words, get_character_count

def get_book_text(file_input):
    # open file
    with open(file_input) as f:
        # read text into variable
        file_text = f.read()
    # return text
    return file_text

def main():
    text = get_book_text("books/frankenstein.txt")
    
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    
    num_characters = get_character_count(text)
    print(num_characters)


if __name__ == "__main__":
    main()