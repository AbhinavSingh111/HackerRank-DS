# given a sorted array , find the first and last occurence of an element .
# since the array is sorted , we will use Binary Search
def first_occ(array,ele):
    first=0
    start = 0
    end = len(array)-1
    while start<=end:
        mid = start + (end-start)//2
        
        if array[mid]==ele:
            first = mid
            end = mid-1
        elif ele<array[mid]:
            end = mid-1
        else:
            start = mid+1
    return first


def last_occ(array,ele):
    last=0
    start = 0
    end = len(array)-1
    while start<=end:
        mid = start + (end-start)//2
        
        if array[mid]==ele:
            last = mid
            start = mid+1
        elif ele<array[mid]:
            end = mid-1
        else:
            start = mid+1
    return last

def fnlocc(array , ele):
    first = first_occ(array,ele)
    last = last_occ(array,ele)
    return [first,last]

 
array = [4,10,10,10,10,18,20]
ele = 10
print(fnlocc(array,ele))



approach 2 : Binary search

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans=[-1,-1]
        if len(nums)==0:
            return ans
        i=0
        j=len(nums)-1

        while i<j:
            m = (i+j)//2
            if nums[m]<target:
                i=m+1
            else:
                j=m
        if nums[i]!=target:
            return ans
        else:
            ans[0]=i
        j=len(nums)-1
        while i<j:
            m = (i+j)//2+1
            if nums[m]>target:
                j=m-1
            else:
                i=m
        ans[1]=j
        return ans
    
approach 3 , for loop traversal O(n)

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first_occ=-1
        last_occ=0
        for i in range(len(nums)):
            if nums[i]<target:
                continue
            if nums[i] == target:
                if first_occ==-1:
                    first_occ=i
                    last_occ=i
                else:
                    last_occ=i
            if nums[i]>target:
                break
        if first_occ==-1:
            last_occ=-1
        return [first_occ , last_occ]

    
    
