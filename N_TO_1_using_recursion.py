# printing N to ! using recursion
# using IBH , induction , base , hypothesis

def n_to_one(N):
    if N==1:
        print(1)
        return
    print(N)
    n_to_one(N-1)
    

N = 5
print(n_to_one(N))


# printing factorial of n using recursion
# using IBH , induction , base , hypothesis

def factorial(N):
    if N==1 or N== 0:
        return 1
    return N * factorial(N-1)
    

N = 10
print(factorial(N))
