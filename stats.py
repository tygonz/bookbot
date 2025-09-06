def get_num_words(text):
    words = text.split()
    return len(words)    

def get_character_count(text):
    character_counts = {}
    for character in text:
        character = character.lower()
        if character not in character_counts:
            character_counts[character] = 1
        else:
            character_counts[character] += 1
    return character_counts

def return_number(unsorted_dict):
    return unsorted_dict["num"]

def sort_dictionary(input_dict):
    new_list = []
    for item in input_dict:
        if not item.isalpha():
            continue
        dict_unit = {}
        dict_unit["char"] = item
        dict_unit["num"] = input_dict[item]
        new_list.append(dict_unit)
    new_list.sort(reverse=True, key=return_number)
    return new_list