//Recursive Fibonacci solution
exports.fibonacciRecursive = fibonacciRecursive;
function fibonacciRecursive(inputNumber) {
    if (inputNumber <= 0) return 0; //0th Fibonacci number is 0
    else if (inputNumber === 1) return 1; //1st Fibonacci number is 1

    //Add previous 2 Fibonacci numbers together to get next number
    return fibonacciRecursive(inputNumber - 2) + fibonacciRecursive(inputNumber - 1);
}

//Iterative Fibonacci solution
exports.fibonacciIterative = function(inputNumber) {
    if (inputNumber === 1) return 1; //1st Fibonacci number is 1
    else if (inputNumber <= 0) return 0; //0th Fibonacci number is 0

    let result = 1; //Will hold nth Fibonacci number
    let previous = 0; //Previous Fibonacci number

    //Loop from 2nd Fibonacci number to nth
    for (let i = 2; i <= inputNumber; i++) {
        let temp = result;
        result += previous; //Next Fibonacci number is sum of current and previous
        previous = temp; //Update previous to old current (was in result)
    }

    return result;
}