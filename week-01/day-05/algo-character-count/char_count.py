import re #Reguluar expressions module

#Return list of character counts that are not spaces or punctuation

#List is sorted by count descending then alphabetically
def char_count(string):
    #Remove all spaces, underscores, and non-alphanumeric characters
    #from string then sort the string characters alphabetically
    string = sorted(re.sub("\W|_|\s", "", string))

    #Iterate through all characters in the string and increment
    #the count for the character in the map
    char_map = {}
    for ch in string:
        if ch not in char_map:
            char_map[ch] = 1
        else:
            char_map[ch] += 1

    #Convert the character map to a list where each key-value
    #pair is an element in the array and sort them by count
    char_list = [[i, j] for i, j in dict.items(char_map)]
    char_list.sort(reverse=True, key=lambda a: a[1])

    return char_list