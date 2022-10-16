exports.translate = function(word) {
    let translated = "";
    for (w of word.split(" ")) {
        let vowel = /a|e|i|o|u/.test(w[0]);
        if (vowel) translated += w + "ay ";
        else {
            let vowelFound = false;
            for (let i = 0; i < w.length; i++) {
                if (/a|e|i|o|u/.test(w[i])) {
                    vowelFound = true;
                    translated += w.substring(i, w.length) + w.substring(0, i) + "ay ";
                }
            }

            if (!vowelFound) translated += w + "ay "
        }
    }
    return translated;
}
console.log(exports.translate("say"))