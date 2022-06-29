# kadne's algorithm , it gives O(n) , 
# it traverses along the array and keeps on calculationg the sum contagiously. the moment overall sum
# gets negative it changes the value of sum=0 , and continues.
def maxSubArray( nums):
    max_s=-999999
    s=0
    for i in nums:
        s=s+i
        if s>max_s:
            max_s=s
        if s<0:
            s=0        
    return max_s
nums=[-57,9,-72,-72,-62,45,-97,24]
print(maxSubArray(nums))
