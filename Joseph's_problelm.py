# solving Joseph's problem using recursion
# the problem is that there are certain number of people , all have to kill each other , find out the one who will be left out to do suicide.

# we will solve if by using IBH

def Murder(arr, k ,sword ):
    if len(arr)==1:
        print(arr[0])
        return
    sword = (sword + k )%len(arr)
    arr.pop(sword)
    Murder(arr, k ,sword )

    



arr = [i for i in range(1, 41)]
k = 6 #we have done k-- , initial k =7
sword =0
print(Murder(arr, k ,sword ))
