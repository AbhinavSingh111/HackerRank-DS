# here we are trying to generate balanced brackets problem with recurion .
# if n = 2 then op should be : "(())","()()"

def generate_balanced_brackets(open , close , op):
    if open==0 and close==0:
        print(op)
        return
    if open!=0:
        op1 = op 
        op1+="("
        generate_balanced_brackets(open-1 , close , op1)
    if close>open:
        op2 = op 
        op2+= ")"
        generate_balanced_brackets(open , close-1 , op2)

ip = 10
op=""
open = ip
close = ip
print(generate_balanced_brackets(open , close , op))

