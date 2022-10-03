#Basic linear search, return index of first object instance in array
def linear_search(obj, arr):
    result = None #Index of obj in arr, None if not found

    #Iterate through every element in array
    for i in range(0, len(arr)):
        #Set result to current index if element is equal to obj,
        #exit loop as we only want first instance
        if arr[i] == obj:
            result = i
            break

    return result

#Global linear search, return array of all indices where obj 
#appears in input array
def linear_search_global(obj, arr):
    results = [] #Holds all indices of obj in arr

    #Iterate through every element in input array and add the index
    #to results array anytime obj is found
    for i in range(0, len(arr)):
        if arr[i] == obj:
            results.append(i)
    
    return results