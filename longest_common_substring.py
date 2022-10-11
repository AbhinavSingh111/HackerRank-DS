# it is a variation of LCS , here we have to find substring instead of subsequence
# approach 3 : top down dp

def longest_common_substring(arr1 , arr2 , length1 , length2):
    dp = [[0 for i in range(length2+1)]for j in range(length1+1)]
    m = -99999999
    for i in range(length1+1):
        for j in range(length2+1):
            if i==0 or j==0:
                dp[i][j] = 0
            elif arr1[i-1]==arr2[j-1]:
                dp[i][j] = 1+dp[i-1][j-1]
            else:
                dp[i][j] = 0
            if dp[i][j]>m:
                m=dp[i][j]
    return m
arr1 = "abcfifjlefoppfj,oig;easjorgrjhiogreorijofjroifj"
arr2 = "abcfifjlefoppfj,oig;easjorgrjhiogre"
length1 = len(arr1)
length2 = len(arr2)
print(longest_common_substring(arr1, arr2 , length1 , length2))
