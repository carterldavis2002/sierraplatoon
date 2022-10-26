import math
import re

def factorial(x):
    return 1 if x <= 1 else factorial(x - 1) * x

def palindrome(string):
    def helper(string, idx):
        return (True if idx > len(string) / 2 
                     else string[idx] == string[len(string) - idx - 1] and helper(string, idx + 1))
    
    return helper(re.sub("\W|_|\s", "", str(string).lower()), 0) 

def bottles(num):
    def helper(num, start):
        if num <= 0:
            print("No more bottles of beer on the wall, no more bottles of beer.")
            print(f"Go to the store, and buy some more, {'no more' if start < 0 else start} bottle{'' if start == 1 else 's'} of beer on the wall.")
            return

        print(f"{num} bottle{'' if num == 1 else 's'} of beer on the wall, {num} bottle{'' if num == 1 else 's'} of beer.")
        print(f"Take one down and pass it around, {'no more' if num - 1 == 0 else num - 1} bottle{'' if num - 1 == 1 else 's'} of beer on the wall.\n")

        helper(num - 1, start)

    helper(num, num)

def roman_num(num):
    def helper(num, map, str):
        if len(map) == 0: return str

        arabic = map[0][1]
        divisible = math.floor(num / arabic)
        if divisible >= 1:
            str += map[0][0] * divisible
            num -= arabic * divisible
        
        return helper(num, map[1:], str)

    map = [["M", 1000], ["CM", 900], ["D", 500], ["CD", 400], ["C", 100], ["XC", 90], ["L", 50], ["XL", 40], ["X", 10], ["IX", 9], ["V", 5], ["IV", 4], ["I", 1]]
    return helper(num, map, "")

def roman_num_alt(num):
    map = [["M", 1000], ["CM", 900], ["D", 500], ["CD", 400], ["C", 100], ["XC", 90], ["L", 50], ["XL", 40], ["X", 10], ["IX", 9], ["V", 5], ["IV", 4], ["I", 1]]

    for a, b in map:
        if num >= b:
            return a + roman_num_alt(num - b)

    return ""

print(roman_num_alt(944))