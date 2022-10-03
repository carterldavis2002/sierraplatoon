#Recursive Fibonacci solution
def fibonacci_recursive(input_number):
    if input_number <= 0: return 0 #0th Fibonacci number is 0
    elif input_number == 1: return 1 #1st Fibonacci number is 1

    #Add previous 2 Fibonacci numbers together to get next number
    return fibonacci_recursive(input_number - 2) + fibonacci_recursive(input_number - 1)

#Iterative Fibonacci solution
def fibonacci_iterative(input_number):
    if input_number == 1: return 1 #1st Fibonacci number is 1
    elif input_number <= 0: return 0 #0th Fibonacci number is 0

    result = 1 #Will hold nth Fibonacci number
    previous = 0 #Previous Fibonacci number

    #Loop from 2nd Fibonacci number to nth
    for _ in range(2, input_number + 1):
        temp = result
        result += previous #Next Fibonacci number is sum of current and previous
        previous = temp #Update previous to old current (was in result)
    
    return result