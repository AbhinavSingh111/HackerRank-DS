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


# or 
def maxProfit(prices): #take every trancsaction that gives profit , ie , all byu at all dips and sell at all peaks
    max_p=0
    bd=0 #cbuying date
    sd=0 #selling date
    for i in range(1,len(prices)):
        if prices[i]>=prices[i-1]: #checks if the next price is greater , if yes then move sd ahead
            sd+=1
        else: #if not then collect the profit and move both buying and sell date
            max_p+=prices[sd]-prices[bd]
            bd=i
            sd=i
    max_p+=prices[sd]-prices[bd]
    return max_p
    
prices=[3,1,4,8,7,2,5]
print(maxProfit(prices))
