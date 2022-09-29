# here we are trying subset problem with recurion .
# same problem has been tried with other approaches in file named subset_leetcode78.py

# same can be used for list with minor changes

# problems like print all subsets , power subsets , unique subsets , all subsequence are variations of the subset problem



def subset(ip,op):
    if len(ip)==0:
        print(op)
        return
    op1 = op 
    op2 = op
    op2  += ip[0]
    ip  = ip[1::]
    subset(ip,op1)
    subset(ip,op2)

ip = "abc"
op=""
print(subset(ip,op))

