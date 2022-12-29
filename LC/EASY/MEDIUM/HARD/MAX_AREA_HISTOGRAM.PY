https://leetcode.com/problems/largest-rectangle-in-histogram/description/
84. Largest Rectangle in Histogram


# Intuition
# when we look we find that we can expand to left and right from a given element untill we find a smaller ele than current ele

# this gives us hint to use NSR and NSL

# Approach
# area = height*(NSR-NSL-1)

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
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
