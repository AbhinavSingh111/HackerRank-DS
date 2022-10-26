# the question Next Greater Element is also asked as Next Greater to Right

# questions like:
# 1> next greater to left
# 2> next greater to right /  Next Greater Element
# 3> nearest smaller to left / nearest smaller element 
# 4> nearest smaller to right 

# these all 4 questions are based on same approach and concepts and based on these standard questions further questions can be solved

# refer to diary notes for more 

# it is a stack based question
# identification is that if the second loop of depends on the first loop (j depends on i in a On^2 soln ) then the question will use a stack for an optimized soln

# Given an array arr[ ] of size N having elements, the task is to find the next greater element for each element of the array in order of their appearance in the array.
# Next greater element of an element in the array is the nearest element on the right which is greater than the current element.
# If there does not exist next greater of current element, then next greater element for current element is -1. For example, next greater of the last element is always -1.

# link to ques
# https://practice.geeksforgeeks.org/problems/next-larger-element-1587115620/1?utm_source=gfg&utm_medium=article&utm_campaign=bottom_sticky_on_article


def nextLargerElement(arr,n):
    #code here
    stack = []
    vector = []
    for i in range(n-1 , -1 , -1):
        if len(stack)==0:
            vector.append(-1)
        elif len(stack)>0 and arr[i]<stack[-1]:
            vector.append(stack[-1])
        elif len(stack)>0 and arr[i]>=stack[-1]:
            while len(stack)>0 and arr[i]>=stack[-1]:
                stack.pop()
            if len(stack)==0:
                vector.append(-1)
            else:
                vector.append(stack[-1])
        stack.append(arr[i])
    return vector[::-1]

arr = [1,3,2,4]
print(nextLargerElement(arr , len(arr)))
