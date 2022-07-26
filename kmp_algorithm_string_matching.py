# this program returns the index of occurance of a substring in a string , 
# this program uses KMP algorithm

def kmp(haystack , needle):
    if needle == "": return 0
    ln = len(needle)
    lps = [0]*ln
    previousLPS , i = 0 , 1
    while i < ln:
        if needle[previousLPS]==needle[i]:
            lps[i]=previousLPS+1
            previousLPS+=1
            i+=1
        elif previousLPS ==0:
            lps[i]=0
            i+=1
        else:
            previousLPS = lps[previousLPS-1]
    i = 0 #for haystack
    j = 0 #for needle
    lh = len(haystack)
    while i<lh:
        if haystack[i]==needle[j]:
            i+=1
            j+=1
        else:
            if j==0:
                i+=1
            else:
                j = lps[j-1]
        if j==ln:
            return i-ln
    return -1
needle = "aaaa"
haystack = "aaacaaaa"
print(kmp(haystack,needle))

# code is also present in leetcode 28 submission and vs
