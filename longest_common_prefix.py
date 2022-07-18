def longestCommonPrefix(strs):
    ans=""
    l = len(min(strs))
    for i in range(l):
        c=strs[0][i]
        for j in range(1,len(strs)):
            if c!=strs[j][i]:
                return ans
        ans+=c
    return ans

    # another approach
    res = ""
    for i in zip(*strs): 
        if(len(set(i)) != 1):
            return res
        res += i[0]      
    return res


strs=  ["flower","flow","flight"]
print(longestCommonPrefix(strs))
