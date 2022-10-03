#Returns list of all Armstrong Numbers from input list
def find_armstrong_numbers(numbers):
    armstrong_nums = [] #Holds found Armstrong Numbers

    #Iterate through every number in the input list
    for i in numbers:
        num_string = str(i) #String representation of current number
        length = len(num_string) #String length of current number (# of digits)

        if i < 0: continue #Armstrong Number must be positive

        #All single digit numbers are Armstrong Numbers
        if length == 1:
            armstrong_nums.append(i)
            continue

        sum = 0 #Sum of all digits raised to power of number length

        #Iterate through every digit in number string and add to sum
        for j in range(0, length):
            sum += int(num_string[j]) ** length

        #Add to Armstrong Number list if the sum is the same as the current
        #input number
        if sum == i:
            armstrong_nums.append(i)
        
    return armstrong_nums