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
