# total ways to decode a string
#  given that string will not begin with 0 or any invalid character
#  ex , 123 =a,ab,abc,aw

def ways(string):
    dp = [0 for i in range(len(string))]
    dp[0]=1
    for i in range(1,len(dp)):
        if string[i-1]=='0' and string[i]=='0': #last_two='00'
            # that means no move can be made , so just put 0
            dp[i]=0
        elif string[i-1]=='0' and string[i]!='0': #last_two='0NonZero'
            # this means that we can use only i and not i-1 and i together , in this case put the i-1 value
            dp[i]=dp[i-1]
        elif string[i-1]!='0' and string[i]=='0': #last_two='NonZero0'
            # this means that we can use only  i-1 and i together , not i alone
            # in this case we first check if the string forming is less than or equal to 26
            if string[i-1]=='1' or string[i-1]=='2':
                # if the length of string is not lesss than 2
                if i>=2:
                    #  then we have to take the value prior to nonzero , ie i-2 , 2310-> 23-10
                    dp[i]=dp[i-2]
                else:
                    #  if the length of string is less than 2 then , we just put 1
                    dp[i]=1
            else:
                # if the string is bigger than 26 then now way is there , so 0
                dp[i]=0
        else:
            # last_two='NonZeroNonZero
            # in this case we first check if the string forming is less than or equal to 26
            if string[i-1]=='1' or string[i-1]=='2':
                if i>=2:
                    # if the length of string is not lesss than 2
                    #  in case the string is less or equal to 26 and length of string is >=2
                    # then we take the sum of 2 values prior to 1
                    dp[i]=dp[i-1]+dp[i-2]
                else:
                    #  if the length of string is less than 2 then , we just take i-1 and add 1 to it
                    dp[i]=dp[i-1]+1
            else:
                # if the last_two is greater than 26 , then jsut put the i-1
                dp[i]=dp[i-1]
    # return the last value 
    return dp[-1]


string = '231011'
print(ways(string))
