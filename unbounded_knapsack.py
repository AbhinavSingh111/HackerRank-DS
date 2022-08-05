def unbounded_knapsack(weights , values , capacity):
    dp = [0 for i in range(capacity+1)]
    dp[0]=0
    for bagcapacty in range(1,(capacity+1)):
        m=0
        for i in range(len(weights)):
            if weights[i]<=bagcapacty:
                rem_bag_capacity = bagcapacty-weights[i]
                rem_value = dp[rem_bag_capacity]
                total_value = rem_value+values[i]
                if  total_value>m:
                    m=total_value
        dp[bagcapacty]=m
    return dp[capacity]
    # this is similar to coin change subset.(both combination and permutation can be used until we dont have
    # to print the pattern ) 
# do look at target sum subset , coin change 
    
       









weights=[2 , 5, 1 , 3 , 4]
values =[15 , 14 ,10 , 45 , 30]
# weights=[83,84, 85, 76 ,13 ,87, 2, 23, 33, 82, 79, 100, 88, 85, 91, 78, 83, 44, 4, 50 ,11 ,68 ,90, 88, 73, 83, 46, 16, 7, 35, 76, 31, 40, 49, 65, 2, 18, 47, 55, 38, 75, 58, 86, 77, 96, 94, 82, 92, 10, 86, 54, 49, 65, 44, 77, 22, 81, 52]
# values =[57, 95, 13 ,29 ,1 ,99, 34, 77, 61, 23, 24, 70, 73, 88, 33, 61, 43, 5, 41, 63, 8, 67, 20, 72, 98, 59, 46, 58, 64, 94, 97, 70, 46, 81, 42, 7, 1, 52, 20, 54, 81, 3, 73, 78, 81, 11, 41, 45, 18, 94, 24, 82, 9, 19, 59, 48, 2, 72]

capacity= 7
print(unbounded_knapsack(weights,values,capacity))
