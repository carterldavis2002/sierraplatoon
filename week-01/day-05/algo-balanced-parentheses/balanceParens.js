//LeetCode #20 - Valid Parentheses
exports.balanceParens = function(s) {
    let stack = []; //Stack for open parentheses types
    
    //Iterate through all characters in input string
    for (let i = 0; i < s.length; i++) {

        //Add to stack if character is open parentheses type
        if (s[i] === "{" || s[i] === "[" || s[i] === "(")
            stack.push(s[i]);
        
        //Character was a closed parentheses type if nothing
        //was added to stack, cant have closed before open
        if (stack.length === 0)
            return false;
        
        //If closed is encountered, pop top item off stack
        //and if the popped open doesn't match the closed type, the
        //string is invalid
        if (s[i] === ")" && stack.pop() !== "(")
            return false;
        else if (s[i] === "]" && stack.pop() !== "[")
            return false;
        else if (s[i] === "}" && stack.pop() !== "{")
            return false;
    }
    
    //Stack items may be leftover if they were more open than closed
    return stack.length === 0;
}