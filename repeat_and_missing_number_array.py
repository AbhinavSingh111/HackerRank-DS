        l=[]
        c=[0]*len(A)
        for i in range(len(A)):
            if c[A[i]-1] !=0:
                c[A[i]-1]+=1
            else:
                c[A[i]-1]=1

        l.append(c.index(2)+1)
        l.append(c.index(0)+1)
        
        return l

# another approach
        N=len(A)
        asum=sum(A)
        nsum=N*(N+1)//2
        k=asum-nsum
        x=asum-sum(set(A))
        return [x,x-k]
A=[3, 1 ,2 ,5 ,3] 

print(repeatedNumber(A))
