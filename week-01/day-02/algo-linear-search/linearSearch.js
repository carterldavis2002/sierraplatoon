//Basic linear search, return index of first object instance in array
exports.linearSearch = function(obj, arr) {
    let result = undefined; //Index of obj in arr, undefined if not found
    
    //Iterate through every element in array
    arr.forEach((item, idx) => {
        //Set result to current index if obj is found and
        //result was not set previously
        if (item === obj && result === undefined) result = idx;
    });

    return result;
}

//Global linear search, return array of all indices where obj 
//appears in input array
exports.linearSearchGlobal = function(obj, arr) {
    let results = []; //Holds all indices of obj in arr

    //Iterate through every element in input array and add the index
    //to results array anytime obj is found
    arr.forEach((item, idx) => {
        if(item === obj) results.push(idx);
    });

    return results;
}