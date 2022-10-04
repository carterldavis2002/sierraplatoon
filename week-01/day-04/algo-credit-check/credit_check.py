#Return validation status of number string through the Luhn algorithm
def credit_check(input_str):
    sum = 0 #Total sum of manipulated digits

    #Iterate through all digits in number string
    for i in range(len(input_str) - 1, -1, -1):

        #Only double every other digits in the string
        num = int(input_str[i]) if i % 2 == 1 else int(input_str[i]) * 2

        #If doubled digit is 10 or more, number to add is the sum
        #of the digits 
        if num > 9:
            num = int(str(num)[0]) + int(str(num)[1])

        #Add calculated number to sum
        sum += num

    #Number string is valid if sum of manipulated digits is divisible by 10
    return "The number is valid!" if sum % 10 == 0 else "The number is invalid!"