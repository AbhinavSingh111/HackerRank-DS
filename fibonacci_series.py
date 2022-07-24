def fibonacci_series(n,second_last,last):
    if n-1==0:
        return last
    else:
        new_last=second_last+last
        second_last=last
        return fibonacci_series(n-1,second_last,new_last)

def fibonacci_series_other_method(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci_series_other_method(n-1)+fibonacci_series_other_method(n-2)
    
    
 def fibonacci_by_dp_memoization(n,bank):
    if n==1:
        return 1
    elif n==0:
        return 0
    elif bank[n]!=0:
        return bank[n]
    else:
        print("function called")
        fib = fibonacci_by_dp_memoization(n-1,bank)+fibonacci_by_dp_memoization(n-2,bank)
        bank[n]=fib
        return fib

if __name__=="__main__":
    n = 10
    print(n)
    print(fibonacci_series(n,0,1))
    print(fibonacci_series_other_method(n))
    print(fibonacci_by_dp_memoization(n,bank))
