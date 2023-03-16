https://practice.geeksforgeeks.org/problems/0960a833f70b09c59444ea487f99729929fc8910/1

class Solution():
    def solver(self,length):
        l = ((length+1)*(length))//2
        return l
        
    def no_of_subarrays(self, n,arr):
        #your code goes here
        count=0
        l=0
        for i in arr:
            if i==0:
                count+=1
            else:
                l+=self.solver(count)
                count=0
        l+=self.solver(count)
        return l
