https://leetcode.com/problems/maximal-rectangle/description/
85. Maximal Rectangle

# Intuition
# this question is as same as max rectangle in a histogram.
# The difference is that in previous question we had 1D array here we have 2D
# we change 2d in 1d and apply the logic of max rectangle in a histogram

# Approach
# WE will make a function that will take 1D array and return the max area of histogram for that array.

# we will repeat the same process for each 1d arr present in the matrix and then return the max area.

# for the 1st array in matrix we pass it as it is.
# from second onwards we add the elements of second arr to the previous arr and if we encounter a 0 in second arr we make the whole element 0


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def moh(heights):
            right = [] #to find Nearest Smaller to left
            left = [] #to find Nearest Smaller to right
            s = [] #temporary stack

            # finding NSL
            for i in range(len(heights)):
                if len(s)==0:
                    left.append(-1)
                elif len(s)>0 and heights[s[-1]]<heights[i]:
                    left.append(s[-1])
                elif len(s)>0 and heights[s[-1]]>=heights[i]:
                    while len(s)>0 and heights[s[-1]]>=heights[i]:
                        s.pop()
                    if len(s)==0:
                        left.append(-1)
                    else:
                        left.append(s[-1])
                s.append(i)

            #finding NSR
            s=[] 
            for i in range(len(heights)-1,-1,-1):
                if len(s)==0:
                    right.append(len(heights))
                elif len(s)>0 and heights[s[-1]]<heights[i]:
                    right.append(s[-1])
                elif len(s)>0 and heights[s[-1]]>=heights[i]:
                    while len(s)>0 and heights[s[-1]]>=heights[i]:
                        s.pop()
                    if len(s)==0:
                        right.append(len(heights))
                    else:
                        right.append(s[-1])
                s.append(i)
            right = right[::-1]

            #finding MAX rectangle possible
            area = -1
            for i in range(len(heights)):
                temp_area = heights[i]*(right[i]-left[i]-1)
                if temp_area>area:
                    area = temp_area

            return area

<!-- converting 2d matrix into chunks of 1d array and then passing it to maximum area of histogram function -->
        m = 0
        k=[]
        for i in range(len(matrix)):
            p = [eval(j) for j in matrix[i]]
            if i==0:
                ar = moh(p)
                k=p
            else:
                for l in range(len(p)):
                    if p[l]==0:
                        k[l]=0
                    else:
                        k[l]+=p[l]
            ar = moh(k)
            if ar>m:
                m=ar
        return m
