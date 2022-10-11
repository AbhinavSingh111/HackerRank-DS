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
