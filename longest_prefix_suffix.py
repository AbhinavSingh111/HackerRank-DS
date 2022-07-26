# longest-prefix-suffix
def lps(s):
    lps=[0]*len(s)
    prevLPS,i=0,1
    while i < len(s):
        if s[prevLPS]==s[i]:
            lps[i]=prevLPS+1
            prevLPS+=1
            i+=1
        elif prevLPS==0:
            lps[i]=0
            i+=1
            
        else:
            prevLPS = lps[prevLPS-1]
    ps=""
    for i in range(lps[-1]):
        ps+=s[i]
    return ps
    # in case only length is asked
    return lps[-1]

s="abab"
print(lps(s))
