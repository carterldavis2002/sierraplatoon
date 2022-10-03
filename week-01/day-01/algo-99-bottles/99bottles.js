function bottleSong(startNum = 99) {
    let currentNum = startNum; //Current number of bottles left

    //Print number of bottles until there are none left
    while (currentNum > 0) {
        console.log(`${currentNum} bottle${currentNum == 1 ? '' : 's'} of beer on the wall, ${currentNum} bottle${currentNum == 1 ? '' : 's'} of beer.`);
        console.log(`Take one down and pass it around, ${currentNum - 1 == 0 ? 'no more' : currentNum - 1} bottle${currentNum - 1 == 1 ? '' : 's'} of beer on the wall.\n`);
        
        currentNum--; //Decrement number of bottles by 1
    }

    //Print no more bottles when currentNum == 0
    console.log("No more bottles of beer on the wall, no more bottles of beer.");
    console.log(`Go to the store, and buy some more, ${startNum < 0 ? 'no more' : startNum} bottle${startNum == 1 ? '' : 's'} of beer on the wall.`);
}

bottleSong(200);