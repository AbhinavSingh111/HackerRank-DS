# Input: Intervals = {{1,3},{2,4},{6,8},{9,10}}
# Output: {{1, 4}, {6, 8}, {9, 10}}
# Explanation: Given intervals: [1,3],[2,4],[6,8],[9,10], we have only two overlapping intervals here,[1,3] and [2,4]. Therefore we will merge these two and return [1,4],[6,8], [9,10].

# Input: Intervals = {{6,8},{1,9},{2,4},{4,7}}
# Output: {{1, 9}} 

def mergeIntervals(intervals):
    # approach using stack

    # intervals.sort()
    # stack=[]
    # stack.append(intervals[0])
    # for i in intervals[1:]:
    #     if stack[-1][1]>=i[0] :
    # if completely falls within the prev interval
    #         if i[1]<=stack[-1][1]:
    #             continue
    #         else:
    #             stack[-1][1]=i[1]
    # if partially overlaps
    #     else:
    #         stack.append(i)
    # return stack

# aproach using inplace updation
    intervals.sort()
    index=0
    for i in intervals[1:]:
        # checking for overlap
        if intervals[index][1]>=i[0]:
            if i[1]<=intervals[index][1]:
                # if completely falls within the prev interval
                intervals.remove(i)
                continue
            else:
                # if partially overlaps
                intervals[index][1]=i[1]
                intervals.remove(i)
        else:
            index+=1
            
        
    return intervals



arr = [[6, 8], [1, 9], [2, 4], [4, 7]]
# arr=[[1,3],[2,4],[6,8],[9,10]]
# arr=[[1,3],[2,6],[4,7],[11,15],[14,18]]
print(mergeIntervals(arr))

   









