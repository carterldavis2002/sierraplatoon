//Returns array of all Armstrong Numbers from input array
exports.findArmstrongNumbers = function(arr) {
    let armstrongNums = []; //Holds found Armstrong Numbers

    //Iterate through every number in the input array
    arr.forEach((item) => {
        let numString = item.toString(); //String representation of current number
        let length = numString.length; //String length of current number (# of digits)

        //All single digit numbers are Armstrong Numbers
        if (length === 1) {
            armstrongNums.push(item);
            return;
        }

        let sum = 0; //Sum of all digits raised to power of number length

        //Iterate through every digit in number string and add to sum
        for (let i = 0; i < length; i++)
            sum += (+numString[i]) ** length;

        //Add to Armstrong Number array if the sum is the same as the current
        //input number
        if (sum === item) armstrongNums.push(item);
    });

    return armstrongNums;
}