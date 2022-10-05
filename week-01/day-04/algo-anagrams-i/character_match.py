def is_character_match(string1, string2):

    #Holds character counts for each string
    character_map_1 = {}
    character_map_2 = {}

    #Remove spaces from each string
    string1 = "".join(string1.split(" "))
    string2 = "".join(string2.split(" "))

    #Populate character_map_1 with string1 characters
    for ch in string1:
        ch = ch.lower()
        if ch not in character_map_1:
            character_map_1[ch] = 1
        else:
            character_map_1[ch] += 1

    #Populate character_map_2 with string2 characters
    for ch in string2:
        ch = ch.lower()
        if ch not in character_map_2:
            character_map_2[ch] = 1
        else:
            character_map_2[ch] += 1

    #Not an anagram if a character in character_map_1 is
    #not in character_map_2 or doesn't have the same count
    for key in character_map_1:
        if (key not in character_map_2 or 
            character_map_1[key] != character_map_2[key]):
            return False

    #Not an anagram if a character in character_map_2 is
    #not in character_map_1 or doesn't have the same count
    for key in character_map_2:
        if (key not in character_map_1 or 
            character_map_1[key] != character_map_2[key]):
            return False
    
    return True