import re #Import regular expressions module

#Return true if word/sentence/number is a palindrome
def palindrome(word):
    reversed = [*re.sub("\W|_|\s", "", str(word).lower())]
    reversed.reverse()
    reversed = "".join(reversed)
    return re.sub("\W|_|\s", "", str(word).lower()) == reversed