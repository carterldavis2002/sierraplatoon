//Recursive factorial solution
exports.factorialRecursive = factorialRecursive;
function factorialRecursive(inputNumber) {
    return inputNumber <= 1 ? 1 : factorialRecursive(inputNumber - 1) * inputNumber;
}