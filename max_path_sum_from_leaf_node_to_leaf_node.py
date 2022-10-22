# https://practice.geeksforgeeks.org/problems/maximum-path-sum/1

def maxPathSum(self,root):
    res = -9999999
    def solve(root):
        nonlocal res
        if(root==None):
            return 0
        if(root.left == None and root.right == None):
            return root.data
        l = solve(root.left)
        r = solve(root.right)
        
        if(root.left==None):
            return (root.data+r)
        if(root.right==None):
            return (root.data+l)
        temp = max(l, r) + root.data
        ans = l+r+root.data
        res = max(res, ans)

        return temp
    
    if(root==None):
        return 0
    if(root.left==None and root.right==None):
        return root.data
    
    x = solve(root)
    if(root.left==None or root.right==None):
        return max(res, x)
    
    return res
