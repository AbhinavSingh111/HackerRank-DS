cube = lambda x: x*x*x

def fibonacci(n):
    l=[]
    if n-1==0:
        return [0]
    else:
        i=0
        j=1
        for a in range(n):
            if a==0:
                l.append(i)
            elif a==1:
                l.append(j)
            else:
                s=i+j
                l.append(s)
                i=j
                j=s
    return l
#  or
    lis = [0,1]
    for i in range(2,n):
        lis.append(lis[i-2] + lis[i-1])
    return(lis[0:n])
        
    


if __name__ == '__main__':
