# longest-substring-without-repeating-characters

def lengthOfLongestSubstring(arr):
    l=0
    res=0
    s=set()
    for r in range(len(arr)):
        while arr[r] in s:
            s.remove(arr[l])
            l+=1
        s.add(arr[r])
        res = max(res,r-l+1)
    return res



# arr="abcabcdeabcdefghiab"
# arr="bbbbb"
# arr="au"
# arr="dvdf"
# arr="abcabcbb"
arr="pwwkew"
print(lengthOfLongestSubstring(arr))

