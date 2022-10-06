//Returns input array with value appended to array until the
//array's length is equal to minSize
exports.pad = function(array, minSize, value = null) {

    //Copy array and add value to the copy until the length is minSize
    let newArray = array.slice();
    while (newArray.length < minSize) newArray.push(value);

    return newArray; //Return padded array copy
}