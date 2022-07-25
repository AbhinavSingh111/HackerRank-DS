def subset(nums):
# approach 1: cascading , 
# take an empty op array , then run a loop for nums 
    n=len(nums)
    op = [[]]
    for num in nums:
        op+=[curr+[num] for curr in op]
    return op

    # approach 2 backtracking
def subset_backtracking(nums):
    def backtrack(first = 0, curr = []):
        # if the combination is done
        if len(curr) == k:  
            output.append(curr[:])
            return
        for i in range(first, n):
            # add nums[i] into the current combination
            curr.append(nums[i])
            # use next integers to complete the combination
            backtrack(i + 1, curr)
            # backtrack
            curr.pop()
    
    output = []
    n = len(nums)
    for k in range(n + 1):
        backtrack()
    return output
    # approach 3 , lexcographical binary sorted using bit mask
def subsets_bitmask(nums):
    n = len(nums)
    output = []
    
    for i in range(2**n, 2**(n + 1)):
        # generate bitmask, from 0..00 to 1..11
        bitmask = bin(i)[3:]
        
        # append subset corresponding to that bitmask
        output.append([nums[j] for j in range(n) if bitmask[j] == '1'])
    
    return output



nums = [1,2,3]
# print(subset(nums))
# print(subset_backtracking(nums))
print(subsets_bitmask(nums))
