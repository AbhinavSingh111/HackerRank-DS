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



# using o(1)space complexity
stack=[]
min_ele = 0

def push(ele):
    global min_ele
    if len(stack)==0 :
        stack.append(ele)
        min_ele = ele
    else:
        if ele<min_ele:
            f = (2*ele)-min_ele
            stack.append(f)
            min_ele=ele
        else:
            stack.append(ele)
    

def pop():
    global min_ele
    if len(stack)==0:
        return -1
    else:
        if stack[-1]<min_ele:
            min_ele = (2*min_ele)-stack[-1]
            stack.pop()
        else:
            stack.pop()
    



def get_top():
    global min_ele
    if len(stack)==0:
        return -1
    else:
        if stack[-1]<min_ele:
            return (2*min_ele)-stack[-1]   
        else:
            return stack[-1]


def get_min():
    global min_ele
    if len(stack)==0:
        return -1
    else:
        return min_ele

def min_stack(arr):
    push(arr[0])
    push(arr[1])
    push(arr[2])
    push(arr[3])
    # pop()
    # pop()
    # pop()
    return get_min()

arr = [18,19,29,15,16]
print(min_stack(arr))





https://leetcode.com/problems/min-stack/description/
    155. Min Stack

Intuition
WE CAN USE VARIABLES TO KEEP THE TIME COMPLEXITY CONSTANT

Approach
we make a global variable min_ele
and if the value of current element is less then min_ele then in the stack we append 2*(curr_ele)-min_ele
and update the value of min_ele with curr_ele

no while popping it will act as a flag , ie whenever in the stack we will encounter a value smaller than the min_ele
we will have to update the min_ele by using (2*min_ele-stack[-1])
and then pop the stack

Complexity
Time complexity:
Space complexity:
Code
class MinStack:

    def __init__(self):
        self.s=[]
        self.min_ele = None
        

    def push(self, val: int) -> None:
        if len(self.s) == 0:
            self.min_ele=val
            self.s.append(val)
        elif val<self.min_ele:
            self.s.append(2*val-self.min_ele)
            self.min_ele = val
        else:
            self.s.append(val)

        

    def pop(self) -> None:
        if len(self.s)==0:
            return
        elif self.s[-1]<self.min_ele:
            self.min_ele = 2*self.min_ele-self.s[-1]
            self.s.pop()
        else:
            self.s.pop()
        

    def top(self) -> int:
        if len(self.s)==0:
            return -1
        elif self.s[-1]<self.min_ele:
            return self.min_ele
        else:
            return self.s[-1]
        

    def getMin(self) -> int:
        if len(self.s)==0:
            return -1
        else:
            return self.min_ele
        
