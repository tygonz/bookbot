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