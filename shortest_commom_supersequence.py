# length of shortest common supersequence 
# given 2 strings , make a string with all the characters common in both the strings with shortest possible length
# m+n-lcs , where m is the length of the first string and n is the length of second string and lcs is the length of longest common subsequence


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


def shortest_common_supersequence(arr1 , arr2 , length1 , length2):
    lcs_len = lcs(arr1 , arr2 , length1 , length2)
    scs_len = length1+length2-lcs_len
    return scs_len

# arr1 = "adkfjopedefjfdfbdsmcjdkalfuynufiuyfnugnuygff7ufdybdcyinfg7yifbytfmrd6df"
# arr2 = "fedfdopfjpodferfhewmioxthfesftesystuntugrerscyhdcrtcuiyijuctdvftctgtecrutysrtie"
# arr1 = "AGGTAB"
# arr2 =  "GXTXAYB"
arr1="abcdaf"
arr2="acbcf"
length1 = len(arr1)
length2 = len(arr2)
print(shortest_common_supersequence(arr1, arr2 , length1 , length2))




# print_shortest_common_supersequence

def lcs(arr1 , arr2 , length1 , length2):
    dp = [[-1 for i in range(length2+1)]for j in range(length1+1)]
    for i in range(length1+1):
        for j in range(length2+1):
            if i==0 or j==0:
                dp[i][j]=0
            elif arr1[i-1]==arr2[j-1]:
                dp[i][j] = 1+dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i][j-1] , dp[i-1][j])
    return dp

def pscs(arr1 , arr2 , length1 , length2):
    s=""
    dp = lcs(arr1 , arr2 , length1 , length2)
    i , j = length1 , length2
    while i>0 and j>0:
        if arr1[i-1]==arr2[j-1]:
            s+=arr1[i-1]
            i-=1
            j-=1
        else:
            
            if dp[i][j-1]>dp[i-1][j]:
                s+=arr2[j-1]
                j-=1
            else:
                s+=arr1[i-1]
                i-=1
    while i>0:
        s+=arr1[i-1]
        i-=1
    while j>0:
        s+=arr2[j-1]
        j-=1
    return s[::-1]

# arr1 = "AGGTAB"
arr1="abcdaf"
arr2="acbcf"
# arr2 = "GXTXAYB"
length1 = len(arr1)
length2 = len(arr2)
print(pscs(arr1, arr2 , length1 , length2))
