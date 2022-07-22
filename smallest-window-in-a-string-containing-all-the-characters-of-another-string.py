def smallestWindow(s,p):
    dicp = {}
    dics = {}
    for i in p:
        # dicp[i]+=1
        if i in dicp:
            dicp[i]+=1
        else:
            dicp[i]=1
    ans=""
    mc=0
    dmc=len(p)
    i,j=-1,-1
    while(True):
        f1=False
        f2=False
        # acquire
        while i<len(s)-1 and mc<dmc:
            i+=1
            c=s[i]
            if c in dics:
                dics[c]+=1
            else:
                dics[c]=1
            if dics.get(c,0)<=dicp.get(c,0):
                mc+=1
            f1=True
        # collect answer and release
        while j<i and mc==dmc:
            pans = s[j+1:i+1]
            if len(ans)==0 or len(pans)<len(ans):
                ans=pans
            j+=1
            d = s[j]
            if dics[d]==1:
                dics.pop(d)
            else:
                dics[d]-=1
            if dics.get(d,0)<dicp.get(d,0):
                mc-=1
            f2=True
        if f1==False and f2==False:
            break
    return ans


# s= "timetopractice"
# p= "toc"
s = "zoomlazapzo"
p = "oza"
print(smallestWindow(s,p))
