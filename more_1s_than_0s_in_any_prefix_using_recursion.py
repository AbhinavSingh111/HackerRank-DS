# here we are trying to generate N digit binary string having more 1s than 0s in any prefix using  recurion .
# if n = 3 then op should be : "111",110","101"

def binary_String(zeroes , ones , op, n):
    if n == 0 :
        print(op)
        return
    if ones>zeroes:
        op2 = op 
        op2+= "0"
        binary_String(zeroes+1 , ones , op2, n-1)
    op1 = op 
    op1+="1"
    binary_String(zeroes , ones+1 , op1, n-1)


n = 3
op=""
zeroes = 0
ones = 0
print(binary_String(zeroes , ones , op, n))
