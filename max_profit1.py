def maxProfit(prices):
# approach1
    n=len(prices)
    max_p=0
    min_p=prices[0]
    for i in range(n):
        if prices[i]<min_p:
            min_p=prices[i]
        if prices[i]-min_p>max_p:
            max_p=prices[i]-min_p
    if max_p<=0 or max_p is None:
        return 0
    else:
        return max_p

# approach2

    local_max = []
	m = prices[-1]
	result = 0
	# make the local max list
	for i in reversed(range(len(prices))):
	m = max(prices[i], m)
	local_max.append(m)
	# update the max profit
	for i in range(len(prices)):
	profit = local_max[len(prices) - i - 1] - prices[i]
	if profit > result:
	result = profit
	return result

# approach3

    min_buy = float('inf')
    max_profit = 0
    for price in prices:
        if price < min_buy:
            min_buy = price
        else:
            diff = price-min_buy
            if diff > max_profit:
                max_profit = diff
    return max_profit

prices=[3,1,4,8,7,2,5]
print(maxProfit(prices))
                
