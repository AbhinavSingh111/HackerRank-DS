# tower of hanoi using recursion
def hanoi(n,s,d,h):
    if n==0:
        return
    hanoi(n-1,s,h,d)
    print(f"moving disk {n} from {s} to {d}")
    hanoi(n-1,h,d,s)
    print(f"moving disk {n} from {s} to {d}")
n=3
print(hanoi(n,'s','d','h'))
