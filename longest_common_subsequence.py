# LCS is a standard problem , 14 variations of this problems can be found
# in 2 given strings we have to find the length of longest common subseequence
# subsequence is different from substring , in substring the string should be continous while in subsequence it can be non continous

# approach 1 : recursion

def lcs(arr1 , arr2 , length1 , length2):
    if length1==0 or length2==0:
        return 0
    if arr1[length1-1]==arr2[length2-1]:
        return 1+lcs(arr1 , arr2 , length1-1 , length2-1)
    else:
        return max(lcs(arr1 , arr2 , length1 , length2-1),lcs(arr1 , arr2 , length1-1 , length2))

arr1 = "adkfjopedefjfdfbdsmcjdkal"
arr2 = "fedfdopfjpodferfhewmioxthfe"
length1 = len(arr1)
length2 = len(arr2)
# print(lcs(arr1, arr2 , length1 , length2))

# approach 2 : bottom up memoization

dp = [[-1 for i in range(10001)]for j in range(10001)]
def lcs(arr1 , arr2 , length1 , length2):
    if length1==0 or length2==0:
        return 0
    if dp[length1][length2]!=-1:
        return dp[length1][length2]
    else:
        if arr1[length1-1]==arr2[length2-1]:
            dp[length1][length2] = 1+lcs(arr1 , arr2 , length1-1 , length2-1)
            return dp[length1][length2]
        else:
            dp[length1][length2] = max(lcs(arr1 , arr2 , length1 , length2-1),lcs(arr1 , arr2 , length1-1 , length2))
            return dp[length1][length2]

arr1 = "adkfjopedefjfdfbdsmcjdkalfuynufiuyfnugnuygff7ufdybdcyinfg7yifbytfmrd6df"
arr2 = "fedfdopfjpodferfhewmioxthfesftesystuntugrerscyhdcrtcuiyijuctdvftctgtecrutysrtie"
length1 = len(arr1)
length2 = len(arr2)
# print(lcs(arr1, arr2 , length1 , length2))

# approach 3 : top down dp

def lcs(arr1 , arr2 , length1 , length2):
    dp = [[0 for i in range(length2+1)]for j in range(length1+1)]
    for i in range(length1+1):
        for j in range(length2+1):
            if i==0 or j==0:
                dp[i][j] = 0
            elif arr1[i-1]==arr2[j-1]:
                dp[i][j] = 1+dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j] , dp[i][j-1])

    return dp[length1][length2]

arr1 = "adkfjopedefjfdfbdsmcjdkalfuynufiuyfnugnuygff7ufdybdcyinfg7yifbytfmrd6df"
arr2 = "fedfdopfjpodferfhewmioxthfesftesystuntugrerscyhdcrtcuiyijuctdvftctgtecrutysrtie"
length1 = len(arr1)
length2 = len(arr2)
# print(lcs(arr1, arr2 , length1 , length2))

#  print lcs

def print_lcs(arr1 , arr2 , length1 , length2):
    s=""
    dp = [[0 for i in range(length2+1)]for j in range(length1+1)]
    for i in range(length1+1):
        for j in range(length2+1):
            if i==0 or j==0:
                dp[i][j] = 0
            elif arr1[i-1]==arr2[j-1]:
                dp[i][j] = 1+dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j] , dp[i][j-1])

    i , j = length1 , length2
    while i>=0 and j>=0:
        if arr1[i-1]==arr2[j-1]:
            s+=arr1[i-1]
            i-=1
            j-=1
        else:
            if dp[i-1][j]>dp[i][j-1]:
                i-=1
            else:
                j-=1
    return s[::-1]
arr1 = "adkfjopedefjfdfbdsmcjdkalfuynufiuyfnugnuygff7ufdybdcyinfg7yifbytfmrd6df"
arr2 = "fedfdopfjpodferfhewmioxthfesftesystuntugrerscyhdcrtcuiyijuctdvftctgtecrutysrtie"
length1 = len(arr1)
length2 = len(arr2)
print(print_lcs(arr1, arr2 , length1 , length2))
