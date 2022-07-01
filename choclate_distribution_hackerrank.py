# Given an array of n integers where each value represents the number of chocolates in a packet. Each packet can have a variable number of chocolates. There are m students, the task is to distribute chocolate packets such that: 

# Each student gets one packet.
# The difference between the number of chocolates in the packet with maximum chocolates and packet with minimum chocolates given to the students is minimum.

def get_minimum_diff_choclates(arr_of_choc,num_of_stu):
    mins=9999999
    N=len(arr_of_choc)
    arr_of_choc.sort()
    for i in range(N-num_of_stu+1):
        mins=min(mins , arr_of_choc[i + num_of_stu - 1] - arr_of_choc[i])
    return mins
arr_of_choc= [12, 4, 7, 9, 2, 23, 25, 41, 
30, 40, 28, 42, 30, 44, 48, 
43, 50]
num_of_stu = 7 
print(get_minimum_diff_choclates(arr_of_choc,num_of_stu))
