# reverse  a stack using recursion
# using IBH

def insert(stk , temp):
    if len(stk)==0:
        stk.append(temp)
        return
    ele = stk.pop()
    insert(stk , temp)
    stk.append(ele)
    return stk

def reverse_Stack(stk):
    if len(stk)==0:
        return 
    temp = stk.pop()
    reverse_Stack(stk)
    insert(stk, temp)
    return stk
    
stk = [1,2,3,4,5,6,912,3 , 51]
print(reverse_Stack(stk))
