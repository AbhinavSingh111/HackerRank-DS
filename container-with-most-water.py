def maxArea(height) :
    N=len(height)
    l=0
    r=N-1
    m=0
    while l<r:
        m=max(m,min(height[l],height[r])*(r-l))
        if height[l]<height[r]:
            l+=1
        else:
            r-=1
    return m
heights=[2,3,4,5,18,17,6]
print(maxArea(heights))
