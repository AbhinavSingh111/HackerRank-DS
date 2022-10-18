# Palindrome Partitioning problem
# it is a variation of MCM , (we need to create partition (k) and we do not know the values of k so MCM )
# to solve we use general formula for MCM and customise it according to question
# find i,j  , find base cond , find k and its looping scheme , find out how to deal with temp ans
# given a string , partition it such a way that the number of partitions are minimum and resultant strings are palindrome

# we will need a function that will check if a string is a palindrome or not , to use it as a base condition , since if the string is already is a palindrome then we do not need to create any partition

def is_palindrome(str):
    return str==str[::-1]

# recursive approach

def palindromic_partitioning_recursive(str , i , j):
    if i>=j:
        return 0
    if is_palindrome(str[i:j+1]): #if a string is already palindrome we do not need any partition
        return 0

    ans = 9999999
    for k in range(i,j): #i to j-1
        temp_ans = 1 + palindromic_partitioning_recursive(str , i,k) + palindromic_partitioning_recursive(str , k+1,j)
        if temp_ans<ans:
            ans = temp_ans
    return ans

str = "momos"
print(palindromic_partitioning_recursive(str , 0 , len(str)-1))


# memoized version
dp = [[-1 for i in range(502)]for j in range(502)] #change as per i , j constraints
def palindromic_partitioning_memoized(str , i , j):
    if i>=j:
        return 0
    if is_palindrome(str[i:j+1]): #if a string is already palindrome we do not need any partition
        return 0
    if dp[i][j]!=-1:
        return dp[i][j]
    ans = 9999999
    for k in range(i,j): #i to j-1
        temp_ans = 1 + palindromic_partitioning_memoized(str , i,k) + palindromic_partitioning_memoized(str , k+1,j)
        if temp_ans<ans:
            ans = temp_ans
    dp[i][j] = ans
    return ans
