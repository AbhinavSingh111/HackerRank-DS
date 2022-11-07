# https://leetcode.com/problems/roman-to-integer/


    def romanToInt(s):
        dic ={"I":1,"IV":4,"V":5,"IX":9,"X":10,"XL":40,"L":50,"XC":90,"C":100,"CD":400,"D":500,"CM":900,"M":1000}
        dic_priority = {"I":1 , "V":2 , "X":3 ,"L":4 ,"C":5 , "D":6 ,"M":7}
        ans = 0
        i=0
        while i <= len(s):
            if i==len(s)-1:
                ans+=dic[s[i]]
                break
            elif i==len(s):
                break
            elif dic_priority[s[i]]>=dic_priority[s[i+1]] :
                ans+= dic[s[i]]
                i+=1
            else:
                ans+= dic[s[i:i+2]]
                i+=2
        return ans
                

s="LVIII"
print(romanToInt(s))
