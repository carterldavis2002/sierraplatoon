def bottleSong(startNum = 99):
    currentNum = startNum #Current number of bottles left

    #Print number of bottles until there are none left
    while currentNum > 0:
        print(f"{currentNum} bottle{'' if currentNum == 1 else 's'} of beer on the wall, {currentNum} bottle{'' if currentNum == 1 else 's'} of beer.")
        print(f"Take one down and pass it around, {'no more' if currentNum - 1 == 0 else currentNum - 1} bottle{'' if currentNum - 1 == 1 else 's'} of beer on the wall.\n")
        
        currentNum -= 1 #Decrement number of bottles by 1
    
    #Print no more bottles when currentNum <= 0
    print("No more bottles of beer on the wall, no more bottles of beer.")
    print(f"Go to the store, and buy some more, {'no more' if startNum < 0 else startNum} bottle{'' if startNum == 1 else 's'} of beer on the wall.")

bottleSong(1000)