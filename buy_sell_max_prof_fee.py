# buy and sell with max profit , on selling a transaction fee is involved.
# infinite number of transactions can be done

def max_profit_with_fee(fee,prices):
    obsp = -prices[0]
    ossp = 0
    for i in range(1,len(prices)):
        nbsp = 0
        nssp = 0
        if ossp-prices[i]>obsp:
            nbsp = ossp-prices[i]
        else:
            nbsp = obsp
        if obsp+prices[i]-fee>ossp:
            nssp = obsp+prices[i]-fee
        else:
            nssp = ossp
        obsp = nbsp
        ossp = nssp
    return ossp








# prices= [10,15,17,20,16,18,22,20,22,20,23,25]
prices= [10,20,30]
fee=2
print(max_profit_with_fee(fee,prices))
