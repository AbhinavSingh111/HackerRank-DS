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


# slight variation of same question
def nextLargerElementToRight(self,arr,n):
        stack=[]
        vector=[]
        for i in range(n-1,-1,-1):
            if len(stack)==0:
                vector.append(-1)
            elif len(stack)!=0 and arr[i]<stack[-1]:
                vector.append(stack[-1])
            elif len(stack)!=0 and arr[i]>=stack[-1]:
                while len(stack)!=0 and arr[i]>=stack[-1]:
                    stack.pop()
                if len(stack)==0:
                    vector.append(-1)
                else:
                    vector.append(stack[-1])
            stack.append(arr[i])
        return vector[::-1]

n = 4
arr = [1, 3, 2 ,4]
print(nextLargerElementToRight(n,arr))


# questions like greater to left , smaller to right , smaller to right are variations of this question
