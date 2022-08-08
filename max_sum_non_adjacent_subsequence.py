# Given an array Arr of size N containing positive integers. Find the maximum sum of a subsequence such that no two numbers in the sequence should be adjacent in the array.

def findMaxSum(arr):
    include = arr[0]
    exclude = 0
    for i in range(1, len(arr)):
        # WE CANNOT INCLUDE ON INCLUDE , WE WILL INCLUDE ON EXCLUDE
        new_include = exclude+arr[i]
        #  IN CASE OF EXCLUDE AN ELEMENT , WE TAKE MAX OF PREV INCLUDES AND EXCLUDES
        new_exclude = max(include,exclude)
        include = new_include
        exclude = new_exclude
    return max(include , exclude)

arr = [5, 5, 10, 100, 10, 5]
print(findMaxSum(arr))

