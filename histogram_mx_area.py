# given an array with the heights of histograms . the width of all of them is 1 unit.
# find the maximum area formed .
# for that the both heights adjacent to a histogram should either be larger or equal to it
# find out the nearest smaller to right (index) , take pseudo index as length of array and insert when stack is empty
# find out nearest smaller to left (index) , take pseudo index as -1 of array and insert when stack is empty

# find out the width (right - left -1) and multiply with particular height , return the max height

def nsr(heights):
    stack =[]
    right = []
    pseudo_index=len(heights)
    for i in range(len(heights)-1,-1,-1):
        if len(stack)==0:
            right.append(pseudo_index)
        elif len(stack)!=0 and stack[-1][0]<heights[i]:
            right.append(stack[-1][1])
        elif len(stack)!=0 and stack[-1][0]>=heights[i]:
            while len(stack)!=0 and stack[-1][0]>=heights[i]:
                stack.pop()
            if len(stack)==0:
                right.append(pseudo_index)
            else:
                right.append(stack[-1][1])
        stack.append((heights[i],i))
    return right[::-1]
def nsl(heights):
    stack =[]
    left = []
    pseudo_index=-1
    for i in range(len(heights)):
        if len(stack)==0:
            left.append(pseudo_index)
        elif len(stack)!=0 and stack[-1][0]<heights[i]:
            left.append(stack[-1][1])
        elif len(stack)!=0 and stack[-1][0]>=heights[i]:
            while len(stack)!=0 and stack[-1][0]>=heights[i]:
                stack.pop()
            if len(stack)==0:
                left.append(pseudo_index)
            else:
                left.append(stack[-1][1])
        stack.append((heights[i],i))
    return left
def widths(right,left):
    width = [0]*len(right)
    for i in range(len(right)):
        width[i] = right[i]-left[i]-1
    return width
def area(width,heights):
    ma=-999999
    for i in range(len(width)):
        prod = width[i]*heights[i]
        if (prod)>ma:
            ma=prod
    return ma
def max_area(heights):
    # first find out nearest smaller to right (index)
    right = nsr(heights)
    # now fing out nearest smaller to left (index)
    left = nsl(heights)
    # now find the width
    width = widths(right,left)
    # now find max area and return
    return area(width,heights)

    

heights = [6,2,5,4,5,1,6]
print(max_area(heights))
