def longest_palindromic_substring(arr):
#   approach one
    # reslen = 0
    # s=""
    # for i in range(len(arr)):
    #     l,r=i,i
    #     while l>=0 and r<len(arr) and arr[l]==arr[r]:
    #         if (r-l+1)>reslen:
    #             s = arr[l:r+1]
    #             reslen = r-l+1
    #         l-=1
    #         r+=1
    #     l,r=i,i+1
    #     while l>=0 and r<len(arr) and arr[l]==arr[r]:
    #         if (r-l+1)>reslen:
    #             s = arr[l:r+1]
    #             reslen = r-l+1
    #         l-=1
    #         r+=1
    # return s
# approach 2
        res = ''
        
        for i in range(len(arr)*2-1):
		    # i refers to the "central" (or "mid point" or "pivot") of the palindrome
			# Uses index 0 as central, uses the middle of index 0 and 1 as central and so on
			# idx  0  1  2  3  4 ...
			#     l r
			#      l  r
			#        l r
			#         l  r
			# ...
			
            l, r = i // 2, (i + 1) // 2
            
			# Move the pointers outward to check if they are palidrome
            while l >= 0 and r < len(arr) and arr[l] == arr[r]:
                l -= 1
                r += 1
                
            res = res if len(res) > len(arr[l+1:r]) else arr[l+1:r]
            
        return res
        

arr="babad"
print(longest_palindromic_substring(arr))
