# here we are trying permutation_with_space problem with recurion .
# ex , if we have been given a string "abc" , then we need to print "a_bc","ab_c","abc","a_b_c"

def permutation_with_space_using_recursion(ip,op):
    if len(ip)==0:
        print(op)
        return
    op1 = op 
    op1+="-"
    op1+=ip[0]
    op2 = op
    op2+=ip[0]
    ip  = ip[1::]
    permutation_with_space_using_recursion(ip,op1)
    permutation_with_space_using_recursion(ip,op2)

ip = "abcd"
op=""
op+=ip[0]
ip = ip[1::]
print(permutation_with_space_using_recursion(ip,op))

