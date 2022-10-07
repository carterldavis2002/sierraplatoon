#LeetCode #20 - Valid Parentheses
def balance_parens(s):
    stack = [] #Stack for open parentheses types

    #Iterate through all characters in input string
    for ch in s:

        #Add to stack if character is open parentheses type
        if ch == "{" or ch == "[" or ch == "(":
            stack.append(ch)

        #Character was a closed parentheses type if nothing
        #was added to stack, cant have closed before open
        if len(stack) == 0:
            return False
        
        #If closed is encountered, pop top item off stack
        #and if the popped open doesn't match the closed type, the
        #string is invalid
        if ch == ")" and stack.pop() != "(":
            return False
        elif ch == "]" and stack.pop() != "[":
            return False
        elif ch == "}" and stack.pop() != "{":
            return False          

    #Stack items may be leftover if there were more open than closed
    return len(stack) == 0  
