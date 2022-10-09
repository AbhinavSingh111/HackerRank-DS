# target sum subset problem is same as count of subset with given difference  problem 
# the only difference is that in place of diff sum is given , we have to assign +- to elements of array such that their overall sum corresponds to given sum
# on a closer inspection , it is same as count of subset with given difference  problem 
# it is a variation of 01 knapsack and  subset sum count problem
# first we check if the sum of given array and then take out the new sum using equation s1 = (diff+sum(arr))//2
# then we find out the count of subsets having new sum , and that will be out answer : refer to equal sum partition


# also , there is another way which i thought of , ie + means that value is being included in knapsack
# while - indicates that value is not being included
# take the sum of whole array and run for count subset problem
# then search the last element of the row of particular needed sum , the count present is the answer
def target_sum (arr,n,s):
    total_sum = sum(arr)
    half_sum = (s+total_sum)//2
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
s = 1
print(target_sum(arr , n,s))
