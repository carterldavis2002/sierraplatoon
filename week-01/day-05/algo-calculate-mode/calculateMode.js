//Return array of most frequent values in order of appearance
//from input array 
exports.calculateMode = function(arr) {
    //Sorted input array
    let sortedArr = arr.slice().sort();

    let currentCount = 1; //Current element frequency
    let maxCount = 1; //Highest frequency encountered

    //Iterate over all elements in the sorted array
    for (let i = 1; i < sortedArr.length; i++)
    {
        //Increment or reset count depending on if current
        //element is the same as the last
        if(sortedArr[i] == sortedArr[i - 1]) currentCount++;
        else currentCount = 1;

        //Update highest count when current is greater
        if(currentCount > maxCount) 
            maxCount = currentCount;
    }

    let modeSet = new Set(); //Unique values that appear the most

    //Iterate over all possible pairs in original input array
    for (let i = 0; i < arr.length; i++) {
        currentCount = 0; //Reset count of current element

        for (let j = 0; j < arr.length; j++) {
            //Increment count if pair elements are the same
            if (arr[i] === arr[j])
                currentCount++;
        }

        //Add element to modeSet if its frequency matches highest
        if (currentCount === maxCount)
            modeSet.add(arr[i]);
    }

    return Array.from(modeSet); //Convert modeSet to array
}