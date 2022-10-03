import re #Regular expressions module

print("HEY KID!") #Print initial response

goodbyeCount = 0 #Number of times "GOODBYE!" was entered

#Take user input until "GOODBYE!" is entered twice
while True:
    answer = input("> ") #Get input from user

    #User input was empty
    if answer.strip() == "":
        print("WHAT?!")
    #User entered one or more lowercase letters
    elif re.match("[a-z]", answer):
        print("SPEAK UP, KID!")
    #Increment goodbyeCount, print appropriate response,
    #and break from loop if count is 2
    elif answer.strip() == "GOODBYE!":
        print(f"{'LEAVING SO SOON?' if goodbyeCount == 0 else 'LATER, SKATER!'}")
        if goodbyeCount != 0:
            break
        goodbyeCount += 1
    #All uppercase or symbols were entered
    else:
        print("NO, NOT SINCE 1946!")
