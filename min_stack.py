# you are given an array , design an algo such that it converts to min stack , ic every time we call the function it returns the min element present in stack

# using extra space O(n) space complexity
stack=[]
support_stack=[]
def push(ele):
    stack.append(ele)
    if len(support_stack)==0 or ele<=support_stack[-1]:
        support_stack.append(ele)
    



def pop():
    if len(stack)==0:
        return -1
    ans = stack.pop()
    if ans==support_stack[-1]:
        support_stack.pop()



def get_min():
    if len(support_stack)==0:
        return -1
    else:
        return support_stack[-1]


def min_stack(arr):
    push(arr[0])
    push(arr[1])
    push(arr[2])
    push(arr[3])
    pop()
    pop()
    pop()
    return get_min()

arr = [18,19,29,15,16]
print(min_stack(arr))
