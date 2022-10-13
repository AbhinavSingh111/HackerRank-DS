# given a string , find out the Minimum number of insertions in a string to make it a palindrome
# it is a variation of LCS and minimum number of deletions to make a string a palindrome.
# we we analyze closely we will find that the elements we delete to make string a palindrome , if we take one of those elements and 
# insert(in pair) in place of all the elements that need to be deleted then we can convert that string to palindrome
# in summation , number of deletein == number of insertions

# min_ins_req_to_male_stirng_a_palindrome . refer to this ques for further assessment


#  length of longest palindromic subsequence  = LCS(string , reverse(string))
#  minimum number of deletion/insertions = len(string )- length of longest palindromic subsequence

def lcs(arr1, arr2, length1 , length2):
    dp = [[-1 for i in range(length2+1)]for j in range(length1+1)]
    for i in range(length1+1):
        for j in range(length2+1):
            if i==0 or j ==0:
                dp[i][j] = 0
            elif arr1[i-1]==arr2[j-1]:
                dp[i][j] = 1+dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i][j-1],dp[i-1][j])
    return dp[length1][length2]

def longest_palindromic_subsequence(arr):
    return lcs(arr , arr[::-1] , len(arr) , len(arr[::-1]))

def min_ins_req_to_male_stirng_a_palindrome(arr):
    return len(arr)-longest_palindromic_subsequence(arr)

arr = "agbcba"
print(min_ins_req_to_male_stirng_a_palindrome(arr))
