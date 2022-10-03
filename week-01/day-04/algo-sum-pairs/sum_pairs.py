#Returns array of pairs from input array that add up to num
def sum_pairs(arr, num):
    pairs = [] #Holds pairs that add up to sum

    #Iterate over every possible pair of array elements
    for i in range(0, len(arr)):
        for j in range(i + 1, len(arr)):

            #Append pair to pairs array if pair
            #adds up to desired sum
            if arr[i] + arr[j] == num:
                pairs.append([arr[i], arr[j]])

    #Print message if no pairs are found else print the array of found pairs
    print("unable to find pairs") if len(pairs) == 0 else print(pairs)