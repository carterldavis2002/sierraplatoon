//Return list of anagrams between word and words in listOfWords
exports.anagramsFor = function(word, listOfWords) {
    //Remove spaces and transform word to lowercase
    word = getWordLowerNoSpaces(word);

    //Get counts of characters in input word
    let characterMap1 = countCharacters(word);

    //Iterate through all words in input list, getting character
    //counts for each, and add to list if they are anagrams with
    //the input word
    let anagramList = [];
    for (w of listOfWords) {
        let wordNoSpace = getWordLowerNoSpaces(w);
        let characterMap2 = countCharacters(wordNoSpace);

        if(isAnagram(characterMap1, characterMap2)) 
            anagramList.push(w);
    }

    return anagramList;
};

//Return str with no spaces and all lowercase letters
function getWordLowerNoSpaces(str) {
    return str.split(" ").join("").toLowerCase();
}

//Count the characters in word and return map
function countCharacters(word) {
    let characterMap = {};

    for (let i = 0; i < word.length; i++) {
        let ch = word[i];
        if (!characterMap[ch])
            characterMap[ch] = 1;
        else
            characterMap[ch]++;
    }

    return characterMap;
}

//Anagram if both character maps have the
//same characters and counts for them
function isAnagram(charMap1, charMap2) {
    for (key in charMap1) {
        if(charMap1[key] !== charMap2[key])
            return false;
    }

    for (key in charMap2) {
        if(charMap1[key] !== charMap2[key])
            return false;
    }

    return true;
}