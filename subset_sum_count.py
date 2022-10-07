# count sum subsets problem 
# it is a variation of 01 knapsack and subset sum problem
# in subset sum we had to return either true or false , here we have to return the count of subset forming that sum
# 

def subset_sum_count (arr,n,sum):
    dp = [[0 for i in range(sum+1) ]for j in range(n+1)]
    for i in range (n+1):
        for j in range(sum+1):
            if i==0 :
                dp[i][j]=0
            if  j==0 :
                dp[i][j]=1

            elif arr[i-1]<=j:
                dp[i][j] = dp[i-1][j-arr[i-1]] + dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][sum]

# arr=[2 , 3, 7 , 8, 12]
arr=[2 , 3, 5 ,6, 8, 10]
n=len(arr)
sum =10
print(subset_sum_count(arr , n,sum))
