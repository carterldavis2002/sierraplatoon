#Returns input array with value appended to array until the
#array's length is equal to minSize
def pad(array, min_size, value = None):

    #Copy array and add value to the copy until the length is minSize
    newArray = array.copy()
    while len(newArray) < min_size:
        newArray.append(value)

    return newArray #Return padded array copy