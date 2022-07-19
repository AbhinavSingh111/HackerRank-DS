# gfg
# convert-sentence-equivalent-mobile-numeric-keypad-sequence
# my APPROACH

dic={1:[],2:['A','B','C'],3:['D','E','F'],4:['G','H','I'],5:['J','K','L'],6:['M','N','O'],7:['P','Q','R','S']
,8:['T','U','V'],9:['W','X','Y','Z'],0:[" "]}

def sequence(arr):
    for i in arr:
        # print(i)
        for key, value in dic.items():
            if i in value:
                t=value.index(i)+1
                print(str(key)*t,end="")
                break
# arr="GEEKSFORGEEKS"
arr="HELLO WORLD"
sequence(arr)

# another approach / GFG

# Python3 implementation to convert 
# a sentence into its equivalent 
# mobile numeric keypad sequence 

# Function which computes the 
# sequence 
def printSequence(arr, input): 

# length of input string 
	n = len(input) 
	output = "" 
	
	for i in range(n): 
	
		# checking for space 
		if(input[i] == ' '): 
			output = output + "0"
		else: 
			# calculating index for each 
			# character		 
			position = ord(input[i]) - ord('A') 
			output = output + arr[position] 
	# output sequence	 
	return output 
	
# Driver code 
str = ["2", "22", "222", 
	"3", "33", "333", 
	"4", "44", "444", 
	"5", "55", "555", 
	"6", "66", "666", 
	"7", "77", "777", "7777", 
	"8", "88", "888", 
	"9", "99", "999", "9999" ] 

input = "GEEKSFORGEEKS"; 
print( printSequence(str, input)) 

# This code is contributed by upendra bartwal 

