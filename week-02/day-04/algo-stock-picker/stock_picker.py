def picker(prices):
    maxProfit = prices[1] - prices[0]
    indexes = [0, 1]

    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            if prices[j] - prices[i] > maxProfit:
                indexes = [i, j]
                maxProfit = prices[j] - prices[i]
    
    return indexes