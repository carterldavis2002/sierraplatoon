//Return array of character counts that are not spaces or punctuation

//Array is sorted by count descending then alphabetically
exports.charCount = function(str) {
    //Remove all spaces, underscores, and non-alphanumeric characters
    //from string then sort the string characters alphabetically
    str = str.replace(/\W|_|\s/g, "").split("").sort();

    //Iterate through all characters in the string and increment
    //the count for the character in the map
    let charMap = {};
    for (let i = 0; i < str.length; i++) {
        let ch = str[i];
        if (!charMap[ch])
            charMap[ch] = 1;
        else
            charMap[ch]++;
    }

    //Convert the character map to an array where each key-value
    //pair is an element in the array and sort them by count
    return Object.entries(charMap).sort((a, b) => {
        return b[1] - a[1];
    });
};