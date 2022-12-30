https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
150. Evaluate Reverse Polish Notation

Intuition
check if the token can be converted to an integer or not

Approach
if it can be then use those to from the expression

Complexity
Time complexity:
Space complexity:
Code
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i.lstrip("-").isdigit() or i.lstrip("+").isdigit():
                stack.append(i)
            else:
                exp = stack[-2]+i+stack[-1]
                ans = str(int(eval(exp)))
                stack.pop()
                stack.pop()
                stack.append(ans)
        return int(stack[-1])
