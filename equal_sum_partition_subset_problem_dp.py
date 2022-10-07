# equal sum partition  subset sum problem 
# it is a variation of 01 knapsack and subset sum problem
# first we check if the sum of given array is even , if it is even run subset problem for half sum
# if odd then it will never be partitioned into equal subset sum

def equal_sum_partition (arr,n):
    total_sum = sum(arr)
    if total_sum%2!=0:
        return False
    half_sum = total_sum//2
    dp = [[False for i in range(half_sum+1) ]for j in range(n+1)]
    for i in range (n+1):
        for j in range(half_sum+1):
            if i==0 :
                dp[i][j]=False
            if  j==0 :
                dp[i][j]=True

            elif arr[i-1]<=j:
                dp[i][j] = dp[i-1][j-arr[i-1]] or dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][half_sum]

arr=[2 , 3, 7 , 8, 12]
n=len(arr)
print(equal_sum_partition(arr , n))
