# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.z

def longestRepeatingCharSubarray(arr,k):
    dic={}
    res = 0
    l=0
    maxf=0
    for r in range(len(arr)):
        if arr[r] in dic:
            dic[arr[r]]+=1
        else:
            dic[arr[r]]=1
        maxf=max(maxf , dic[arr[r]])
        # while r-l+1 - max(dic.values()) >k:

    # this line takes the length of window and the count of character with highest freq . the difference indicates the number of replacements we can do , and if the difference is within the limits of k , then  it is a valid window and we can proceede further.

    # in this question all we need to do is return the longest length and not actually do the replacement.


    # by using maxf we can reduce the time complexity from (26*n) [ because without maxf whole dic needs to be checked for finding the max fequent charcter which in worst case can be 26 iteration] to (n)
        while r-l+1 - maxf >k:
            dic[arr[l]]-=1
            l+=1
        res = max(r-l+1,res)
    return res




arr="ABABBA"
k=2
print(longestRepeatingCharSubarray(arr,k))
