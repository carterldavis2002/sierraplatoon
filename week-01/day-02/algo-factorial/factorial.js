//Iterative factorial solution
exports.factorialIterative = function(inputNumber) {
    let result = 1n; //Holds final result of factorial

    //Multiply result by current inputNumber val until inputNumber <= 0
    while (inputNumber > 1) {
        result *= BigInt(inputNumber);
        inputNumber--;
    }

    return result;
}

//Recursive factorial solution
exports.factorialRecursive = factorialRecursive;
function factorialRecursive(inputNumber) {
    return inputNumber <= 1 ? 1n : BigInt(factorialRecursive(inputNumber - 1)) * BigInt(inputNumber);
}
