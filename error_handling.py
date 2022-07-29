n=int(input())
for i in range(n):
    a, b=input().split()
    try:
        c= int(a)//int(b)
        print(c)
    except ZeroDivisionError as e :
        print("Error Code:",e)
    except ValueError as e:
        print("Error Code:",e)
