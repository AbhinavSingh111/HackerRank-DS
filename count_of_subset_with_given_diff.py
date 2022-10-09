# count of subset with given difference  problem 
# it is a variation of 01 knapsack and  subset sum count problem
# first we check if the sum of given array and then take out the new sum using equation s1 = (diff+sum(arr))//2
# then we find out the count of subsets having new sum , and that will be out answer : refer to equal sum partition

def count_of_subset_with_given_difference (arr,n,diff):
    total_sum = sum(arr)
    half_sum = (diff+total_sum)//2
    dp = [[0 for i in range(half_sum+1) ]for j in range(n+1)]
    for i in range (n+1):
        for j in range(half_sum+1):
            if i==0 :
                dp[i][j]=0
            if  j==0 :
                dp[i][j]=1

            elif arr[i-1]<=j:
                dp[i][j] = dp[i-1][j-arr[i-1]] + dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][half_sum]

arr=[1,1,2,3]
n=len(arr)
diff = 1
print(count_of_subset_with_given_difference(arr , n,diff))
