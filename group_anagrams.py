from collections import defaultdict
def groupAnagrams(strs):
    dic = defaultdict(list)
    for i in strs:
        key = "".join(sorted(list(i)))
        dic[key].append(i)
    return [l for l in dic.values()]

strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))
        
