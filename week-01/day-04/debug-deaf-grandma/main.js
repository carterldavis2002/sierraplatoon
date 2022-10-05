//Original lines commented out

let isRunning = true;
//Can't use reserved keyword continue as name
//let continue = true

let goodbyes = 0
while (isRunning) {
//while ( continue ) {

    //Moved above loop
    //let goodbyes = 0
    let userInput = prompt()

    if ( userInput == "" ) {
    //if ( userInput = "" ) {
        alert("WHAT!?")
    }
    //Moved from end of loop
    else if ( userInput == "GOODBYE!" ) {
    //else if ( userinput == "GOODBYE!" ) {
        goodbyes++;
        //goodbyes + 1
    
        if ( goodbyes == 1 ) {
            alert("LEAVING SO SOON?");
            //alert("LEAVING SO SOON?')
        }
        else if ( goodbyes == 2 ) {
            alert("LATER, SKATER!")
            isRunning = false;
            //continue = false
        }
    }
    else if ( userInput.toUpperCase() != userInput ) {
    //else if ( userinput.toUppercase != statement ) {
        alert("SPEAK UP, KID!")
    }
    else if ( userInput.toUpperCase() == userInput ) {
    //else if ( statement.toUppercase == statement ) {
        alert('NO, NOT SINCE 1946!')
    }
}