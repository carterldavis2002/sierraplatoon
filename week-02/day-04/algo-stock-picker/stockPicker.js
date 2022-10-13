exports.picker = function(prices) {
    let maxProfit = prices[1] - prices[0];
    let indexes = [0, 1];
    
    for (let i = 0; i < prices.length; i++) {
        for (let j = i + 1; j < prices.length; j++) {
            if (prices[j] - prices[i] > maxProfit) {
                indexes = [i, j];
                maxProfit = prices[j] - prices[i];
            }
        }
    }

    return indexes;
}