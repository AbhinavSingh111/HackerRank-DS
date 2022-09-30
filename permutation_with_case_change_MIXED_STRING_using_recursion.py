# here we are trying permutation_with_case_change_in_a_mixed_string  problem with recurion .
# ex , if we have been given a string "a1b2" , 
# then we need to print "a1b2","a1B2","A1b2","A1B2"

def permutation_with_case_change_in_a_mixed_string(ip,op):
    if len(ip)==0:
        print(op)
        return
    if ip[0].isalpha():
        op1 = op 
        op1+=ip[0].lower()
        op2 = op
        op2+=ip[0].upper()
        ip  = ip[1::]
        permutation_with_case_change_in_a_mixed_string(ip,op1)
        permutation_with_case_change_in_a_mixed_string(ip,op2)
    elif ip[0].isdigit():
        op1 = op 
        op1+=ip[0]
        ip  = ip[1::]
        permutation_with_case_change_in_a_mixed_string(ip,op1)

    
    

ip = "a1b2"
op=""
print(permutation_with_case_change_in_a_mixed_string(ip,op))

