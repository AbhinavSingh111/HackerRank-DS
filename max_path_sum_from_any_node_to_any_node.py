'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    #Function to return maximum path sum from any node in a tree.
    def findMaxSum(self, root): 
        res = -9999999
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
            temp =  max(max(l,r)+root.data , root.data) #store the length when the ans pass through root node , here if the value being returned is negative from both left and right , then we ignore them and take value of root only
            ans = max(temp , root.data+l+r)  #incase the ans does not pass through root node
            res = max(res , ans) #update the ans to get max
            return temp #return in case the ans does not pass through the root of respective sub tree so that it can be used for further calculation
        solve(root)
        return res



#{ 
 # Driver Code Starts
# #Initial Template for Python 3

# #Contributed by Suman Rana
# import sys
# sys.setrecursionlimit(100000)
# from collections import deque
# # Tree Node
# class Node:
#     def __init__(self, val):
#         self.right = None
#         self.data = val
#         self.left = None

    
# # Function to Build Tree   
# def buildTree(s):
#     #Corner Case
#     if(len(s)==0 or s[0]=="N"):           
#         return None
        
#     # Creating list of strings from input 
#     # string after spliting by space
#     ip=list(map(str,s.split()))
    
#     # Create the root of the tree
#     root=Node(int(ip[0]))                     
#     size=0
#     q=deque()
    
#     # Push the root to the queue
#     q.append(root)                            
#     size=size+1 
    
#     # Starting from the second element
#     i=1                                       
#     while(size>0 and i<len(ip)):
#         # Get and remove the front of the queue
#         currNode=q[0]
#         q.popleft()
#         size=size-1
        
#         # Get the current node's value from the string
#         currVal=ip[i]
        
#         # If the left child is not null
#         if(currVal!="N"):
            
#             # Create the left child for the current node
#             currNode.left=Node(int(currVal))
            
#             # Push it to the queue
#             q.append(currNode.left)
#             size=size+1
#         # For the right child
#         i=i+1
#         if(i>=len(ip)):
#             break
#         currVal=ip[i]
        
#         # If the right child is not null
#         if(currVal!="N"):
            
#             # Create the right child for the current node
#             currNode.right=Node(int(currVal))
            
#             # Push it to the queue
#             q.append(currNode.right)
#             size=size+1
#         i=i+1
#     return root
    


# if __name__=="__main__":
#     t=int(input())
#     for _ in range(0,t):
#         root=buildTree(input())
#         ob = Solution()
#         print(ob.findMaxSum(root))
        
        

# } Driver Code Ends
