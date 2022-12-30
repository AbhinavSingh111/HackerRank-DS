https://leetcode.com/problems/car-fleet/description/
853. Car Fleet

Intuition
If the car positioned at the back reaches the target before or at the same time than the car placed before it then they form a fleet

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #using list comprehension to make seperate lists in a list of pairs
        pos = [[p,s] for p,s in zip(position,speed)]
        stack=[]
        # traversing pos in reverse sorted order
        for p,s in sorted(pos)[::-1]:
            stack.append((target-p)/s)
            if len(stack)>=2:
                #we will check if the car having placed behind reaches to destination before the car ahead it , then it will mean that they formed a fleet
                if stack[-1]<=stack[-2]:
                    stack.pop()
        return len(stack)
