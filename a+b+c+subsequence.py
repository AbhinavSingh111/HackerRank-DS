# write a program to count a+b+c+ subsequences in a string 
# note here + is forming a regex expression which denotes one or more than one occurances
# in dp we take characters of string as columns and the a+ , a+b+ , a+b+c+ as rows
# use formula a+ = 2a+1 , a+b+ = 2b+a , a+b+c=2c+b

def count_of_abc_subsequences(string):
    a = 0 # here a denotes a+
    ab = 0 # here ab denotes a+b+
    abc = 0 # here abc denotes a+b+c+
    for i in string:
        if i=='a':
            a=2*a+1
        if i=='b':
            ab = 2*ab + a
        if i=='c':
            abc = 2*abc+ab
    return abc

string = 'abcabc'
print(count_of_abc_subsequences(string))
        
