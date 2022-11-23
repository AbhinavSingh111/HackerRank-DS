https://leetcode.com/problems/pascals-triangle/
118. Pascal's Triangle

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
#         make a list of list as long as the given integer and initialise it by 1s
        res = [[1]*(i+1) for i in range(numRows)]
        for i in range(2, numRows): # starting from 2 coz 0 and 1 are exactly as we need in above list
            for j in range(1, i): #this loop determines how many times we need to traverse previous list
                res[i][j] = res[i-1][j-1] + res[i-1][j] # this statement modifies the current value with respect to values from previous list
        return res
                        
                        
                    
                    
                    
            
        
