def nextSmallerElementToRight(self, arr, n):
    stack=[]
    vector=[]
    for i in range(n-1,-1,-1):
        if len(stack)==0:
            vector.append(-1)
        elif len(stack)!=0 and arr[i]>stack[-1]:
            vector.append(stack[-1])
        elif len(stack)!=0 and arr[i]<=stack[-1]:
            while len(stack)!=0 and arr[i]<=stack[-1]:
                stack.pop()
            if len(stack)==0:
                vector.append(-1)
            else:
                vector.append(stack[-1])
        stack.append(arr[i])
    return vector[::-1]

n = 5
arr = [3, 8, 5, 2, 25]
print(nextSmallerElementToRight(n,arr))
