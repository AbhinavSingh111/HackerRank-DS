

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
        
