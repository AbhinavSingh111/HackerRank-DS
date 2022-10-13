# find out the length of longest repeating subsequence in a string
# this is a variation of LCS
# we take the lcs for the given string , lcs(s1 , s1)
# with the restriction that we add only when i!=j
# the above condition will allow us to only include one of the duplucates to be included and exclude the elements that occur only once

def lrs(arr1 , arr2 , length1 , length2):
    dp = [[-1 for i in range(length2+1)]for j in range(length1+1)]
    for i in range(length1+1):
        for j in range(length2+1):
            if i==0 or j==0:
                dp[i][j] = 0
            elif arr1[i-1]==arr2[j-1] and i!=j:
                dp[i][j] = 1+dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])
    return dp[length1][length2]

arr1 = "AABEBCDD"
print(lrs(arr1 , arr1 , len(arr1) , len(arr1)))
