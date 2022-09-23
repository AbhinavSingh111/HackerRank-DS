# printing 1 to N using recursion
# using IBH , induction , base , hypothesis

def one_to_n(N):
    if N==0:
        return
    one_to_n(N-1)
    print(N)

N = 5
print(one_to_n(N))
