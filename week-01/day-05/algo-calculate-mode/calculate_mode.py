#Return list of most frequent values in order of appearance
#from input list 
def calculate_mode(items):
    #Sorted input array
    sortedList = sorted(items, key=lambda a: str(a))

    currentCount = 1 #Current element frequency
    maxCount = 1 #Highest frequency encountered

    #Iterate over all elements in the sorted list
    for i in range(1, len(sortedList)):

        #Increment or reset count depending on if current
        #element is the same as the last
        if sortedList[i] == sortedList[i - 1]:
            currentCount += 1
        else:
            currentCount = 1
    
        #Update highest count when current is greater
        if currentCount > maxCount:
            maxCount = currentCount

    #Unique values that appear the most
    modeDict = dict()

    #Iterate over all possible pairs in original input array
    for i in items:
        currentCount = 0 #Reset count of current element
        for j in items:

            #Increment count if pair elements are the same
            if i == j:
                currentCount += 1
        
        #Add element to modeDict if its frequency matches highest
        if currentCount == maxCount:
            modeDict[i] = i
    
    return list(modeDict) #Convert modeDict to list