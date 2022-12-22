https://leetcode.com/problems/daily-temperatures/description/
739. Daily Temperatures   

problem similar to next greater element and can be optimized by using stack
1 .Brute force TLE

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer=[]
        for day in range(len(temperatures)):
            count=0
            temp = day+1
            while temp <= len(temperatures):
                if temp == len(temperatures):
                    answer.append(0)
                    break
                elif temperatures[temp]>temperatures[day]:
                    answer.append(count+1)
                    temp+=1
                    break
                else:
                    count+=1
                    temp+=1
        return answer
2 . USING STACK
# we are using the approach to find next greater element just putting indexes in place of element in result stack
class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        s = []
        v = []
        for i in range(len(t)-1,-1,-1):
            if len(s)==0:
                v.append(0)
            elif len(s)>0 and t[s[-1]]>t[i]:
                v.append(s[-1]-i)
            elif len(s)>0 and t[s[-1]]<=t[i]:
                while len(s)>0 and t[s[-1]]<=t[i]:
                    s.pop()
                if len(s)==0:
                    v.append(0)
                else:
                    v.append(s[-1]-i)
            s.append(i)

        return reversed(v)
    
