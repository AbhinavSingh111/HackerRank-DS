

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

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s = []
        v = []
        for i in range(len(temperatures)-1,-1,-1):
            if len(s)==0:
                v.append(0)
            elif len(s)>0 and temperatures[i]<s[-1]:
                v.append(abs(temperatures.index(s[-1])-i))
            elif len(s)>0 and temperatures[i]>s[-1]:
                while len(s)>0 and temperatures[i]>s[-1]:
                    s.pop()
                if len(s)==0:
                    v.append(0)
                else:
                    v.append(abs(temperatures.index(s[-1])-i))
            s.append(temperatures[i])
        return reversed(v)
