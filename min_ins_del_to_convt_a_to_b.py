#  Minimum Number of Insertion and Deletion to convert String a to String b
# it is a variation of LCS
# to find insertion , length1-lcs
# to find deletion , length2-lcs

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


def min_ins_del_to_convt_a_to_b(arr1 , arr2 , length1 , length2):
    lcs_len = lcs(arr1 , arr2 , length1 , length2)
    inserts = length1-lcs_len
    deletions = length2-lcs_len
    print(inserts,deletions) 

# arr1 = "adkfjopedefjfdfbdsmcjdkalfuynufiuyfnugnuygff7ufdybdcyinfg7yifbytfmrd6df"
# arr2 = "fedfdopfjpodferfhewmioxthfesftesystuntugrerscyhdcrtcuiyijuctdvftctgtecrutysrtie"
arr1 = "AGGTAB"
arr2 =  "GXTXAYB"
length1 = len(arr1)
length2 = len(arr2)
min_ins_del_to_convt_a_to_b(arr1, arr2 , length1 , length2)
