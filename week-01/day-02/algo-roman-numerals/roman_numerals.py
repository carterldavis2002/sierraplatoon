import math #Import math module for math.floor()

#Lazy roman numeral conversion, roman numerals are only added together,
#no subtraction involved
def to_roman_lazy(input_number): 
    output = "" #Holds final roman numeral representation

    #Map of roman numeral digits to their arabic equivalents
    roman_numeral_to_arabic_map = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}

    #Iterate over each roman numeral key in the map
    for roman_numeral in roman_numeral_to_arabic_map:

        #Retrieve arabic equivalent from current roman numeral digit
        arabic_number = roman_numeral_to_arabic_map[roman_numeral]

        #Add the roman numeral digit the number of times it's arabic
        #equivalent is divisible by the input number to the output string
        evenly_divisible_times = math.floor(input_number / arabic_number)
        if evenly_divisible_times >= 1:
            output += roman_numeral * evenly_divisible_times
            input_number -= arabic_number * evenly_divisible_times
    
    return output

#Modern roman numeral conversion, smaller numbers that appear before
#larger ones are subtracted from the larger ones
def to_roman_modern(input_number): 
    output = ""
    roman_numeral_to_arabic_map = {"M": 1000, "CM": 900, "D": 500, "CD": 400, "C": 100, "XC": 90, "L": 50, "XL": 40, "X": 10, "IX": 9, "V": 5, "IV": 4, "I": 1}

    for roman_numeral in roman_numeral_to_arabic_map:
        arabic_number = roman_numeral_to_arabic_map[roman_numeral]

        evenly_divisible_times = math.floor(input_number / arabic_number)
        if evenly_divisible_times >= 1:
            output += roman_numeral * evenly_divisible_times
            input_number -= arabic_number * evenly_divisible_times
    
    return output