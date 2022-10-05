//Return true if word/sentence/number is a palindrome
exports.palindrome = function(word) {
    return word.toString().toLowerCase().replace(/\W|_|\s/g, "") 
        === word.toString().toLowerCase().replace(/\W|_|\s/g, "").split("").reverse().join("");
};