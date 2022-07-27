from collections import Counter
def transfiguration( A, B): 
    # # code here 
    la=len(A)
    lb=len(B)
    # if la!=lb:
    #     return -1
    if Counter(A)!=Counter(B):
        return -1
    # dic= [0]*256
    # for i in range(la):
    #     dic[ord(A[i])]+=1
    #     dic[ord(B[i])]-=1
    # if any(dic):
    #     return -1
    res=0
    i=la-1
    j=lb-1
    while i>=0:
        while i>=0 and A[i]!=B[j]:
            i-=1
            res+=1
        if i>=0:
            i-=1
            j-=1
    return res

# without using counter gfg is giving tle

string="ABGH"
into="CDEF"
print(transfiguration(string , into))
