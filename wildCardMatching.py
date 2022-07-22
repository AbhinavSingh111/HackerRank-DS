import re
def match(p,s):
    dp = [[False for i in range(len(s)+1)] for j in range(len(p)+1)]
    for i in reversed(range(len(dp))):
        for j in reversed(range(len(dp[0]))):
            if i==len(dp)-1 and j==len(dp[0])-1:
                dp[i][j]=True
            elif i==len(dp)-1:
                dp[i][j]=False
            elif j==len(dp[0])-1:
                if p[i]=="*":
                    dp[i][j]=dp[i+1][j]
                else:
                    dp[i][j]=False
            else:
                if p[i]=="?":
                    dp[i][j]=dp[i+1][j+1]
                elif p[i]=="*":
                    dp[i][j]=dp[i+1][j] or dp[i][j+1]
                elif p[i]==s[j]:
                    dp[i][j]=dp[i+1][j+1]
                else:
                    dp[i][j]=False
    return dp[0][0]
#     w = ""
#     for i in range(len(p)):
#         if p[i] == "?":
#             w+= r"[a-z]"
#         elif(p[i] == "*"):
#             w+= r"([a-z]*)*"
#         else :
#             w+=p[i]
#     return re.fullmatch(w,s)

            

# p = "ge*ks"
# s = "geeks"
p="***a*b"
s="adceb"
# p="*pqrs"
# s="pqrst"
print(match(p , s))
