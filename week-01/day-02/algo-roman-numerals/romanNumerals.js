//Lazy roman numeral conversion, roman numerals are only added together,
//no subtraction involved
exports.toRomanLazy = function(inputNumber) {
    let output = ""; //Holds final roman numeral representation

    //Map of roman numeral digits to their arabic equivalents
    let romanNumeralToArabicMap = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1};

    //Iterate over each roman numeral key in the map
    for (romanNumeral in romanNumeralToArabicMap) {

        //Retrieve arabic equivalent from current roman numeral digit
        arabicNumber = romanNumeralToArabicMap[romanNumeral];

        //Add the roman numeral digit the number of times it's arabic
        //equivalent is divisible by the input number to the output string
        evenlyDivisibleTimes = Math.floor(inputNumber / arabicNumber);
        if (evenlyDivisibleTimes >= 1) {
            output += romanNumeral.repeat(evenlyDivisibleTimes);
            inputNumber -= arabicNumber * evenlyDivisibleTimes;
        }
    }

    return output;
}

//Modern roman numeral conversion, smaller numbers that appear before
//larger ones are subtracted from the larger ones
exports.toRomanModern = function(inputNumber) {
    let output = "";
    let romanNumeralToArabicMap = {"M": 1000, "CM": 900, "D": 500, "CD": 400, "C": 100, "XC": 90, "L": 50, "XL": 40, "X": 10, "IX": 9, "V": 5, "IV": 4, "I": 1};

    for (romanNumeral in romanNumeralToArabicMap) {
        arabicNumber = romanNumeralToArabicMap[romanNumeral];

        evenlyDivisibleTimes = Math.floor(inputNumber / arabicNumber);
        if (evenlyDivisibleTimes >= 1) {
            output += romanNumeral.repeat(evenlyDivisibleTimes);
            inputNumber -= arabicNumber * evenlyDivisibleTimes;
        }
    }

    return output;
}