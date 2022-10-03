let goodbyeCount = 0; //Number of times "GOODBYE!" was entered
console.log("HEY KID!"); //Initial response

//Continue prompting user until "GOODBYE!" is entered twice
while (true) {
    let input = prompt(); //Get input from user

    //"WHAT?!" response if cancel button was pressed in prompt
    //or no words were entered
    if(input === null || input.trim() === "")
        console.log("WHAT?!");
    //"SPEAK UP, KID!" response if any lowercase letter found
    else if (input.search("[a-z]") != -1)
        console.log("SPEAK UP, KID!");
    //Increment goodbyeCount when "GOODBYE!" is entered
    //and print appropriate response, breaking out of loop if count is 2
    else if (input.trim() === "GOODBYE!") {
        console.log(`${goodbyeCount === 0 ? "LEAVING SO SOON?" : "LATER, SKATER!"}`);
        if(goodbyeCount != 0)
            break;
        goodbyeCount++;
    }
    //All uppercase letters or symbols were entered
    else
        console.log("NO, NOT SINCE 1946!");
}