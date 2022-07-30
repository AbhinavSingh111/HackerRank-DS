# # Python program to compute sum of ranges for different range queries

# import math

# # Function that accepts array and list of queries and print sum of each query
# def queryResults(arr,Q):
	
# 	#Q.sort(): # Sort by L
# 	#sort all queries so that all queries in the increasing order of R values .
# 	Q.sort(key=lambda x: x[1])
	
# 	# Initialize current L, current R and current sum
# 	currL,currR,currSum = 0,0,0
	
# 	# Traverse through all queries
# 	for i in range(len(Q)):
# 		L,R = Q[i] # L and R values of current range
		
# 		# Remove extra elements from previous range
# 		# if previous range is [0, 3] and current
# 		# range is [2, 5], then a[0] and a[1] are subtracted
# 		while currL<L:
# 			currSum-=arr[currL]
# 			currL+=1
			
# 		# Add elements of current range
# 		while currL>L:
# 			currSum+=arr[currL-1]
# 			currL-=1
# 		while currR<=R:
# 			currSum+=arr[currR]
# 			currR+=1
			
# 		# Remove elements of previous range
# 		# when previous range is [0, 10] and current range
# 		# is [3, 8], then a[9] and a[10] are subtracted
# 		while currR>R+1:
# 			currSum-=arr[currR-1]
# 			currR-=1
		
# 		# Print the sum of current range
# 		print("Sum of",Q[i],"is",currSum)

# arr = [1, 1, 2, 1, 3, 4, 5, 2, 8]
# Q = [[0, 4], [1, 3], [2, 4]]
# queryResults(arr,Q)
# #This code is contributed by Shivam Singh


# import math
# def queryResults(arr,Q):
#     n=math.ceil(math.sqrt(len(arr)))
#     sq = [0]*n
#     for i in range(len(arr)):
#         sq[i//n]+=arr[i]
#     # return sq
    
#     for i in Q:
#         sum=0
#         l,r=i
#         q=l
#         e=r
#         # l-=1
#         # r-=1
#         while l<=r:
#             if l%n==0 and l+n-1<=r:
#                 sum+=sq[l//n]
#                 l+=n
#             else:
#                 sum+=arr[l]
#                 l+=1
#         print(f"sum of range {q} to {e} is : ",sum)


# # arr = [1, 1, 2, 1, 3, 4, 5, 2, 8]
# arr= [1, 5 ,-2 ,6 , 8 , -7 ,2 ,1 ,11]
# # Q = [[0, 4], [1, 3], [2, 4]]
# Q = [[1,6],[2,7]]
# queryResults(arr,Q)



import math
def xorQueries(arr, queries):
    n=math.ceil(math.sqrt(len(arr)))
    sq = [0]*n
    ans=[]
    for i in range(len(arr)):
        sq[i//n]^=arr[i]
    
    for i in queries:
        l,r=i
        xored=0
        while l<=r:
            if l%n==0 and l+n-1<=r:
                xored^=sq[l//n]
                l+=n
            else:
                xored^=arr[l]
                l+=1
        ans.append(xored)
    return ans
arr=[15,8,8,8,15]
Q=[[2,2],[3,3]]
print(xorQueries(arr,Q))
                
            
        
