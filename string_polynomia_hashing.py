def strinPolynomialHashing(s):
    p=31
    pow=31
    l=len(s)
    MOD = 10000007
    ans = ord(s[0])-ord('a')+1
    for i in range(1,l):
        ans+=((ord(s[i])-ord('a')+1)*pow)%MOD
        pow*=p%MOD 
    return ans






l=["ab","abc","abcd","abc","xyz","pqr"]
for s in l:
    print(strinPolynomialHashing(s))
