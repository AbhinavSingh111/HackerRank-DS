# in a given array find out the minumum possible difference that is existing between two subsets
# it is a variation of subset sum and very closely resembles to equal sum partition subset problem
# in that problem we had to partition the array into 2 subsets such that the difference of sum of both the partitions be 0
# while in this problem we have to keep that difference minimium
# first we figure out the range between which the sum of two partitions can lie ie 0 , sum(Arr)
# then eleminate those sums from that range which will never be the sum of a subset in actual arr
# we do this by using subset sum method , running it for sum(arr) and then taking the trues from the last row as only those sums will be available in the actual arr possiblse subset
# take only half of the length of that row so as to keep the s1 smaller than s2
# now we need s2 - s1
# for that we can turn above equation to sum(arr)-2s1
# and take the min diff and return


def subset_sum(arr , sum ,n):
    dp = [[False for i in range(sum+1) ]for j in range(n+1)]
    for i in range (n+1):
        for j in range(sum+1):
            if i==0 :
                dp[i][j]=False
            if  j==0 :
                dp[i][j]=True

            elif arr[i-1]<=j:
                dp[i][j] = dp[i-1][j-arr[i-1]] or dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    return dp

def minimum_subset_sum_difference(arr, n):
    dp = subset_sum(arr,sum(arr),n)
    diff = 99999999
    for i in range(1,sum(arr)//2+1):
        if dp[n][i]==True:
            diff  = min(diff ,sum(arr)-2*i )
    return diff

arr = [1 ,2 , 7]
print(minimum_subset_sum_difference(arr , len(arr)))

