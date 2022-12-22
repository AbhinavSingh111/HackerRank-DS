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
3: 
    Here what we are doing is using the constraints given in question to make an array of that size ,
    we will traverse the temperature array from back to front , while doing so , we will search the arr from the current index of temp + 30+1 till end
    if we find any values grater that -1 , it will mean that there are values greater than the tempersature[i] that have been enountered earlier while traversing 
    temperature array
    we will append those values (which are index of the traversed elements from temperature) in a temporary list j
    now if after traversing arr we do not find any value larger than -1 it means that there have been no values greater than current temp value yet traversed ,
    ie len(j)==0 , in that case we will change the value of result array at the particular index(i) to 0
    
    else , we will take the min value from j (which will indicate the recent occurance of an element greater than temperature[i] ) and will substract that with the current index
    to get the difference , and modifty the value in res at current index with the difference 
    
    and in last we will modify the arr[t-30] index of arr with current index.
    
    
    def dailyTemperatures(temperatures):
        arr = [-1 for _ in range(71)]
        res = [0] * len(temperatures)
        
        for i in range(len(temperatures)-1,-1,-1):
            j = []
            t = temperatures[i]
            for x in arr[t-30+1:]:
                if x > -1:
                    j.append(x)
            if len(j) == 0:
                res[i] = 0
            else:
                res[i]=min(j)-i
            arr[t-30] = i

        return(res)



    
