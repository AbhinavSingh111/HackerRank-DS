# given is a 2d sorted array 
# search the given element 
# fix the bounds for i and j , i>=0 and i<=n ,, j>=0 and j<=m
# start from the top right corner , if ele at that is == key , return it
# if key < arr[i][j] , then j-- , ie move to next left col ,as the ele below will not contain key , since they
# are sorted , so we do not visit them 
# if key >  arr[i][j] , then i++ , ie move to next row ele , and at every point we check these cond , until either 
# bounds are met or ele is met , if bounds met , return -1 else return index

def sorted_2d_arr_search(arr,ele):
    i=0
    j=len(arr[0])-1
    while i>=0 and i< len(arr) and j>=0 and j < len(arr[0]):
        if arr[i][j]==ele:
            return [i,j]
        elif arr[i][j]>ele:
            j-=1
        elif arr[i][j]<ele:
            i+=1
    return -1

arr = [[10,20,30,40],[15,25,35,45],[27,29,37,45],[32,33,39,50]]
ele = 12
print(sorted_2d_arr_search(arr,ele))
