# delete the mid element of a stack using recursion
# using IBH

def del_ele(stk , k):
    if k==1:
        stk.pop()
        return stk
    temp = stk.pop()
    del_ele(stk,k-1)
    stk.append(temp)
    return stk

def stack_mid_ele_del_using_rec(stk):
    if len(stk)==0:
        return stk
    k = len(stk)//2 + 1
    del_ele(stk , k)
    return stk
    
stk = [1,2,3,4,5,6]
print(stack_mid_ele_del_using_rec(stk))
