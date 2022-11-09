# https://leetcode.com/problems/roman-to-integer/


def romanToInt( s):
    dic = {"I":1,"IV":4,"V":5,"IX":9,"X":10,"XL":40,"L":50,"XC":90,"C":100,"XD":400,"D":500,"CM":900,"M":1000} # here we are storing all the possible combinations as per the given constrains in problem
    dic_priority = {"I":1 , "V":2 , "X":3 ,"L":4 ,"C":5 , "D":6 ,"M":7} #here we are giving priorities to know which one is bigger , so in case the smaller one comes in front like IV , we can deal it differently
    ans = 0
    i=0
    while i <= len(s): #running the loop till end
        if i==len(s)-1: # if we have reached the last element then we simply put the value of that string from dic and break the loop
            ans+=dic[s[i]]
            break
        elif i==len(s): # if we are somehow reaching beyond last ele , then we break out or we will get index out of bound error
            break
        elif dic_priority[s[i]]>=dic_priority[s[i+1]] : # here we are checking if the current ele has higher  or equal priority than the next , if yes then we simply take the value of current ele form dic and add to the ans
            ans+= dic[s[i]]
            i+=1 # and increase i by 1
        else:
            ans+= dic[s[i:i+2]] # if current ele is smaller than next ele then we take those 2 ele from string and find the corresponding value in dic and then increase the i by 2 , since we have already accessed 2 elementns 
            i+=2
    return ans

s="MCMXCIII"
print(romanToInt(s))
                
