//Returns array of unique pairs from input array that add up to num
exports.sumPairs = function(arr, num) {
    let pairs = []; //Holds pairs that add up to sum

    //Iterate over every possible pair of
    //array elements (no duplicates!)
    for (let i = 0; i < arr.length; i++) {
        for (let j = i + 1; j < arr.length; j++) {

            //Append pair to pairs array if pair
            //adds up to desired sum
            if (arr[i] + arr[j] === num)
                pairs.push([arr[i], arr[j]]);
        }
    }

    //Print message if no pairs are found else
    //print the array of found pairs
    if (pairs.length == 0)
        console.log("unable to find pairs");
    else
        console.log(pairs);
}