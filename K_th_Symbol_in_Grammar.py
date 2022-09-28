# https://leetcode.com/problems/k-th-symbol-in-grammar/     
# question on above link
class Solution:
    def kthGrammar(self , n, k):
        if n==1 and k==1:
            return 0
        mid  = 2**(n-1)//2
        if mid>=k:
            return self.kthGrammar(n-1, k)
        if mid<k:
             return int(not self.kthGrammar(n-1, k-mid))
