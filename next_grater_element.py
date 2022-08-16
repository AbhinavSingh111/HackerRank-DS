# The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.

# You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.


from operator import indexOf


def nextGreaterElementToRight(nums1, nums2):
    stack = []
    vector = []
    for i in range(len(nums1)):
        temp=nums2[nums2.index(nums1[i]):]
        stack=temp[::-1]
        if len(stack)==0:
            vector.append(-1)
        elif len(stack)!=0 and stack[-1]>nums1[i]:
            vector.append(stack[-1])
        elif len(stack)!=0 and stack[-1]<=nums1[i]:
            while len(stack)!=0 and stack[-1]<=nums1[i]:
                stack.pop()
            if len(stack)==0:
                vector.append(-1)
            else:
                vector.append(stack[-1])
    return vector

nums1=[4,1,2]
nums2=[1,3,4,2]
print(nextGreaterElementToRight(nums1,nums2))
