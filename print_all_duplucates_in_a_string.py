# print_all_duplucates_in_a_string

# approach 1

from collections import Counter
def all_duplicates_and_their_freq(arr):
    l= Counter(arr)
    for key,val in l.items():
        if val>=2:
            print(key , val)
# arr="geeksforgeeks"
arr="test string"
all_duplicates_and_their_freq(arr)

# approach 2
def all_duplicates_and_their_freq(arr):
    dic={}
    for i in arr:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1
    for key,val in dic.items():
        if val>=2:
            print(key , val)


arr="geeksforgeeks"
all_duplicates_and_their_freq(arr)

