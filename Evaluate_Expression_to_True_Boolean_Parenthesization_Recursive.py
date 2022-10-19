# Evaluate Expression to True Boolean Parenthesization Recursive
# it is a variation of MCM
# follow the MCM format and change it acc to question
# given a string containing TF|&^ , evaluate the string in such a way that the expression results in T and then return the count of ways

# I think base condition should not return True/False. Since we are calculating number of ways it should return 1) 0 when i>j and 2) 1 when (i==j && str[i] == "T" && isTrue == true) and (i==j && str[i] == "F" && isTrue == false)


def parenthesization(str , i , j , val):
    if i>j:
        return 0
    if i==j:
        if s[i]=="T" and val == True:
            return 1
        elif s[i] == "F" and val == False:
            return 1
        else:
            return 0
    ans = 0
    for k in range(i+1,j,2):
        lt = parenthesization(s , i , k-1  , True)
        lf = parenthesization(s , i , k-1  , False)
        rt = parenthesization(s , k+1 , j  , True)
        rf = parenthesization(s , k+1 , j  , False)
        if s[k] =="&":
            if val == True:
                ans = ans+lt*rt
            else:
                ans = ans+lt*rf+lf*rt+lf*rf
        if s[k]=="|":
            if val == True:
                ans = ans+lt*rt+lt*rf+lf*rt
            else:
                ans = ans+lf*rf
        if s[k]=="^":
            if val == True:
                ans = ans+lt*rf+lf*rt
            else:
                ans = ans+lf*rf+lt*rt
    return ans


s = "T^F|T"
val = True
i = 0
j = len(s)-1
print(parenthesization(s , i , j , val ))
