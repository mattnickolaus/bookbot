
def main():
    path_to_file = 'books/frankenstein.txt'
    book_text = get_book_text(path_to_file)
    letters_dictionary = count_characters(book_text)

    print(f"--- Begin report of {path_to_file} ---")
    print(f"{get_number_of_words(book_text)} words were found in {path_to_file}")
    print()
    sorted_characters_output(letters_dictionary)
    print(f"--- End report ---")


def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def get_number_of_words(string):
    words = string.split()
    return len(words)

def count_characters(string):
    lowered_string = string.lower()
    list_of_characters = list(lowered_string)

    character_dict = {}
    for character in list_of_characters:
        if character not in character_dict:
            character_dict[character] = 1
        else:
            character_dict[character] += 1

    return character_dict

def sort_on_letters(dictionary):
    return dictionary['qty']

def sorted_characters_output(dictionary):
    character_pairs = []
    for key, value in dictionary.items():
        if key.isalpha():
           character_pairs.append({"letter": key, "qty": value})

    character_pairs.sort(reverse=True, key=sort_on_letters)
    for pair in character_pairs:
        print(f"The '{pair['letter']}' character was found {pair['qty']} times.")



main()