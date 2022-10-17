# matrix chain multiplication , is a standard problem with various variations
# this problem contains a general format  , that format varies according to questions
# in these problems we are given with a string or an array ,
# we first decide the position of i and j , generally they are on the left and right sides , respectively
# then we have to find the base condition , first invalid input
# we have to divide the array with a variable k and then define the position and range of k
# based on i  , j , k , we call the recursive function
# each recursive call will give us temporary ans , what we do with that ans depends on the question
# we apply specific functions as per question needs on temp ans to get final ans

# the general format is as follows:
# def solve(arr , i , j):
#     if i<j: #varies acc to ques
#         return 0
#     for k in range(i,j): 
#         temp_ans = solve(arr , i , k) + solve(arr ,k+1 , j) #varies acc to ques
#         ans = fun(temp_ans) #varies acc to ques
#     return ans

# in mcm
# 1 find the position of i and j 
# 2 figure out base cond , first invalid input
# decide the partition  , k
# decide how to treat the temp ans

# in the given array , contains the rows and cols of matrices
# number of matrices  = len(arr)-1
# A[i] = arr[i-1]*arr[i]   # the row and col of a matrix

def mcm(arr , i , j):
    if i>=j:
        return 0
    ans = 9999999
    for k in range(i,j):
        temp_ans = mcm(arr , i , k) + mcm(arr , k+1 , j) + (arr[i-1]*arr[k]*arr[j])
        if temp_ans<ans:
            ans = temp_ans
    return ans

arr = [10,30,5,60]
print(mcm(arr , 1 , len(arr)-1))


# approach 2  , memoization
dp = [[-1 for i in range(10002)]for j in range(10002)]
def mcm(arr , i , j):
    if i>=j:
        return 0
    if dp[i][j]!=-1:
        return dp[i][j]
    ans = 9999999
    for k in range(i,j):
        temp_ans = mcm(arr , i , k) + mcm(arr , k+1 , j) + (arr[i-1]*arr[k]*arr[j])
        if temp_ans<ans:
            ans = temp_ans
    dp[i][j] = ans
    return ans

arr = [10,30,5,60]
print(mcm(arr , 1 , len(arr)-1))

