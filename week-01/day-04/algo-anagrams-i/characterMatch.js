exports.isCharacterMatch = function(string1, string2) {

    //Holds character counts for each string
    let characterMap1 = {};
    let characterMap2 = {};

    //Remove spaces from each string
    string1 = string1.split(" ").join("");
    string2 = string2.split(" ").join("");

    //Populate characterMap1 with string1 characters
    for (let i = 0; i < string1.length; i++) {
        let ch = string1[i].toLowerCase();
        if (!characterMap1[ch])
            characterMap1[ch] = 1;
        else
            characterMap1[ch]++;
    }

    //Populate characterMap2 with string2 characters
    for (let i = 0; i < string2.length; i++) {
        let ch = string2[i].toLowerCase();
        if (!characterMap2[ch])
            characterMap2[ch] = 1;
        else
            characterMap2[ch]++;
    }

    //Not an anagram if a character in characterMap1 is
    //not in characterMap2 or doesn't have the same count
    for (key in characterMap1) {
        if(characterMap1[key] !== characterMap2[key])
            return false;
    }

    //Not an anagram if a character in characterMap2 is
    //not in characterMap1 or doesn't have the same count
    for (key in characterMap2) {
        if(characterMap1[key] !== characterMap2[key])
            return false;
    }
    
    return true;
};