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

# USING STACK

https://leetcode.com/problems/generate-parentheses/description/
22. Generate Parentheses

Intuition
USING RECURSION

Approach
only add open parenthesis if open<n
only add close parenthesis of close<open
return when open==close==n -->

Complexity
Time complexity:
Space complexity:
Code
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # only add open parenthesis if open<n
        # only add close parenthesis of close<open
        # return when open==close==n
        stack = []
        res = []
        def rec(open , close):
            if open==close==n:
                res.append("".join(stack))
            if open<n:
                stack.append("(")
                rec(open+1 ,close)
                stack.pop()
            if close<open:
                stack.append(")")
                rec(open, close+1)
                stack.pop()
        rec(0,0)
        return res

