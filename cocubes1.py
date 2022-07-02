a,p=[],[]
for i in range(0,6):
    a.append(int(input()))
q=len(a)-1
for i in range(0,len(a)):
    count=0
    for j in range(i+1,len(a)):
        if a[i]<a[j]:
            count=0
            break
        else :
            count+=1
    if count!=0:
        p.append(a[i])
p.append(a[q])
print(p)
