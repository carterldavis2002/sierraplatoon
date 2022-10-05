#Return list of anagrams between word and words in list_of_Words
def anagrams_for(word, list_of_words):
    #Remove spaces and transform word to lowercase
    word = get_word_lower_no_spaces(word)

    #Get counts of characters in input word
    character_map_1 = count_characters(word)

    #Iterate through all words in input list, getting character
    #counts for each, and add to list if they are anagrams with
    #the input word
    anagram_list = []
    for w in list_of_words:
        word_no_space = get_word_lower_no_spaces(w)
        character_map_2 = count_characters(word_no_space)
    
        if (isAnagram(character_map_1, character_map_2)):
            anagram_list.append(w)

    return anagram_list

#Return str with no spaces and all lowercase letters
def get_word_lower_no_spaces(str):
    return "".join(str.split(" ")).lower()

#Count the characters in word and return map
def count_characters(word):
    character_map = {}

    for ch in word:
        if ch not in character_map:
            character_map[ch] = 1
        else:
            character_map[ch] += 1
    
    return character_map

#Anagram if both character maps have the
#same characters and counts for them
def isAnagram(char_map_1, char_map_2):
    for key in char_map_1:
        if (key not in char_map_2 or 
            char_map_1[key] != char_map_2[key]):
            return False

    for key in char_map_2:
        if (key not in char_map_1 or 
            char_map_1[key] != char_map_2[key]):
            return False

    return True