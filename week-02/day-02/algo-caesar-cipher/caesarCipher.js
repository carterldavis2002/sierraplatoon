exports.caesarCipher = function(str, num) {
    let result = "";
    for (let i = 0; i < str.length; i++) {
        console.log(Number(str.charCodeAt(i)))
        console.log(Number(str.charCodeAt(i) + num))
        if (/[A-Z]/i.test(str[i]))
            result += String.fromCharCode(str.charCodeAt(i) + num);
        else
            result += str[i];
    }
    return result;
}
console.log(exports.caesarCipher("What a string!", 5))