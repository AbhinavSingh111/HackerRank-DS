# buy and sell with max profit , on selling a cooldown of 1 day is mandatory before buying.
# infinite number of transactions can be done
# buy and sell with max profit , on selling a transaction fee is involved.
# infinite number of transactions can be done

def max_profit_with_cooldown(prices):
    obsp = -prices[0]
    ossp = 0
    ocsp = 0
    for i in range(1,len(prices)):
        nbsp = 0
        nssp = 0
        ncsp = 0
        if ocsp-prices[i]>obsp:
            nbsp = ocsp-prices[i]
        else:
            nbsp = obsp
        if obsp+prices[i]>ossp:
            nssp = obsp+prices[i]
        else:
            nssp = ossp
        if ossp > ocsp:
            ncsp = ossp
        else:
            ncsp = ocsp
        obsp = nbsp
        ossp = nssp
        ocsp = ncsp
    return ossp

# prices= [10,15,17,20,16,18,22,20,22,20,23,25]
prices= [10,20,30]
print(max_profit_with_cooldown(prices))
