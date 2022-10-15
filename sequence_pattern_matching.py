# sequence pattern matching , in this problem return of str1 is a subsequence of str2
# to do so find lcs of both strings and if the length of lcs == len(str1) ,. then return true
# this is a variation of lcs but this can be done with recursion also and a few variations of spm problems can also be formed

def lcs(arr1 , arr2 , length1 , length2):
    dp = [[-1 for i in range(length2+1)]for j in range(length1+1)]
    for i in range(length1+1):
        for j in range(length2+1):
            if i==0 or j==0:
                dp[i][j] = 0
            elif arr1[i-1]==arr2[j-1]:
                dp[i][j] = 1+dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])
    return dp[length1][length2]

def spm(arr1 , arr2):
    len_lcs  = lcs(arr1 , arr2 , len(arr1) , len(arr2))
    if len_lcs == len(arr1):
        return True
    else:
        return False

arr1 = "AYX"
arr2 = "ABYCDFXYZQP"
print(spm(arr1 , arr2))
    
