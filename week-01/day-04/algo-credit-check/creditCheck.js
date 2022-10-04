//Return validation status of number string through the Luhn algorithm
exports.creditCheck = function(str) {
    let sum = 0; //Total sum of manipulated digits

    //Iterate through all digits in number string
    for (let i = str.length - 1; i >= 0; i--) {

        //Only double every other digits in the string
        let num = i % 2 === 1 ? +str[i] : (+str[i]) * 2;

        //If doubled digit is 10 or more, number to add is the sum
        //of the digits 
        if (num > 9) 
            num = (+num.toString()[0]) + (+num.toString()[1]);

        sum += num; //Add calculated number to sum
    }

    //Number string is valid if sum of manipulated digits is divisible by 10
    return sum % 10 === 0 ? "The number is valid!" : "The number is invalid!";
}