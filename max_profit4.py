def maxProfit(k, prices) :
    if not prices:
        return 0 
    N=len(prices)
    if N<=1 or k<=0:
        return 0
    profit=0
    if N//2<=k:
        for i in range(N-1):
            if prices[i]<prices[i+1]:
                profit+=prices[i+1]-prices[i]
        return profit
                

    A=[float('-inf')]*k
    B=[0]*k
    for price in prices:
        for j in range(k):
            if j==0:
                A[j]=max(A[j],0-price )
            else:
                A[j]=max(A[j],B[j-1]-price)
            B[j]=max(B[j],A[j]+price)
    return B[k-1]
prices= [3,2,6,5,0,3]
k=2
print(maxProfit(k,prices))



# approach 2
# it has n^3 complexity
def maxProfit(k, prices) :
    dp = [[0 for i in range(len(prices))] for i in range(k+1)]
    for t in range(1,k+1):
        for d in range(1,len(prices)): #will run for all prices
            m = dp[t][d-1] # m is being initialised with a value which means if the particular transactions have been completed a day before today
            for p in range(d): # also we take into account all the n-1 transactions + the nth transactions possible and then take the max value out of them as answer and place it in dp[t][d]
                pt = dp[t-1][p]+(prices[d]-prices[p])
                if pt>m:
                    m=pt
            dp[t][d]=m
    return dp[k][len(prices)-1]





prices= [3,2,6,5,0,3]
k=2
print(maxProfit(k,prices))


# approach 3
# it has n^2 complexity
# here we store the max values in 2nd loop only so no need to run 3rd loop
def maxProfit(k, prices) :
    dp = [[0 for i in range(len(prices))] for i in range(k+1)]
    for t in range(1,k+1):
        m = -999999
        for d in range(1,len(prices)): #will run for all prices // dp[t][d] = max(dp[t][d-1]vs
            # max(dp[t-1][d-1]-prices[d-1])+prices[d])
            if dp[t-1][d-1]-prices[d-1]>m:
                m=dp[t-1][d-1]-prices[d-1]
            if m+prices[d]>dp[t][d-1]:
                dp[t][d]=m+prices[d]
            else:
                dp[t][d]=dp[t][d-1]

    return dp[k][len(prices)-1]





prices= [3,2,6,5,0,3]
k=2
print(maxProfit(k,prices))
