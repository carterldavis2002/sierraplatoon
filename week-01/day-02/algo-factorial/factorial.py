#Iterative factorial solution
def factorial_iterative(input_number):
    result = 1 #Holds final result of factorial

    #Multiply result by current inputNumber val until inputNumber <= 0
    while input_number > 1:
        result *= input_number
        input_number -= 1
    
    return result

#Recursive factorial solution
def factorial_recursive(input_number):
    return 1 if input_number <= 1 else factorial_recursive(input_number - 1) * input_number