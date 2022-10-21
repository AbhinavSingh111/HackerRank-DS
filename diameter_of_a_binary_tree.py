# https://practice.geeksforgeeks.org/problems/diameter-of-binary-tree/1
class Solution:
    
    #Function to return the diameter of a Binary Tree.
    
    def diameter(self,root):
        res = 0
        def solve(root):
            nonlocal res # here the reason for using nonlocal (Specific to python 3 
            # is that it will restrict solve(root) from creating a local copy of res . 
            # it will make solve() modify the outer res 
            # , we can also declare and use res as res=[0] , which will make it mutable)
            # If the enclosing scope that counter is defined in is not the global scope, 
            # on Python 3.x you could use the nonlocal statement. In the same situation on Python 2.x 
            # you would have no way to reassign to the nonlocal name counter, 
            # so you would need to make counter mutable and modify it:
            
            
            #base
            if root is None:
                return 0
              
             #hypothesis
            l = solve(root.left) 
            r = solve(root.right)
            
            #induction 
            
            temp = 1 + max(l,r)   #store the length when the ans pass through root node
            ans = max(temp , 1+l+r) #incase the ans does not pass through root node
            res = max(res , ans) #update the ans to get max
            return temp #return in case the ans does not pass through the root of respective sub tree so that it can be used for further calculation
        solve(root)
        return res
        
