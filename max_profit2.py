def maxProfit(prices):
    max_p=0
    # l=sorted(prices)
    # if prices==l.reverse() or prices==l:
    #     return 0
    for i in range(len(prices)-1):
        if prices[i]<prices[i+1]:
            max_p+=prices[i+1]-prices[i]
    return max_p
prices=[3,1,4,8,7,2,5]
print(maxProfit(prices))
