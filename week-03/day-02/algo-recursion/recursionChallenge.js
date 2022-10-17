exports.factorial = function(inputNumber) {
    return inputNumber <= 1 ? 1 : exports.factorial(inputNumber - 1) * inputNumber;
};

exports.palindrome = function(word) {
    function helper(word, idx) {
        return idx > word.length / 2 ? true :
            word[idx] === word[word.length - idx - 1] && helper(word, ++idx);
    }

    return helper(word.toString().toLowerCase().replace(/\W|_|\s/g, ""), 0);
};

exports.bottles = function(num) {
    function helper(num, start) {
        if (num <= 0) {
            console.log("No more bottles of beer on the wall, no more bottles of beer.");
            console.log(`Go to the store, and buy some more, ${start < 0 ? 'no more' : start} bottle${start == 1 ? '' : 's'} of beer on the wall.`);
            return;
        }

        console.log(`${num} bottle${num == 1 ? '' : 's'} of beer on the wall, ${num} bottle${num == 1 ? '' : 's'} of beer.`);
        console.log(`Take one down and pass it around, ${num - 1 == 0 ? 'no more' : num - 1} bottle${num - 1 == 1 ? '' : 's'} of beer on the wall.\n`);

        helper(--num, start);
    }

    helper(num, num);
};

exports.romanNum = function(num) {
    function helper(num, map, str) {
        if (map.length == 0) return str;

        arabic = map[0][1];
        divisible = Math.floor(num / arabic);
        if (divisible >= 1) {
            str += map[0][0].repeat(divisible);
            num -= arabic * divisible;
        }
        map.shift();

        return helper(num, map, str);
    }

    let map = [["M", 1000], ["CM", 900], ["D", 500], ["CD", 400], ["C", 100], ["XC", 90], ["L", 50], ["XL", 40], ["X", 10], ["IX", 9], ["V", 5], ["IV", 4], ["I", 1]];
    return helper(num, map, "");
};