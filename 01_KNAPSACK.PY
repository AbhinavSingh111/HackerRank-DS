def knapsack(weights , values , capacity):
    dp = [[0 for i in range(capacity+1)]for i in range(len(weights)+1)]
    for i in range(1,len(dp)):
        for j in range(1,len(dp[0])):
        # starting form 1 because the first row and column will all have 0

            # checking if weight to be put is less or equal to current capacity
            # in cricket analogy , if the number of balls he will definetly play is less or equal to current available balls
            #  that is if he is gonna bat or not
            if j>=weights[i-1]:
                # if he plays 
                rem_weights = j-weights[i-1] #checking remaining balls
                if dp[i-1][rem_weights]+values[i-1]>dp[i-1][j]: #if the runs made by his prior team on left balls+ the runs he will make > the runs made by his team if he did not bat
                   dp[i][j]=dp[i-1][rem_weights]+values[i-1] 
                else:
                    dp[i][j]=dp[i-1][j]

            else:
            # if he does not bat , 
            #  then just put the score the team before him made
               dp[i][j]=dp[i-1][j]
    return dp[len(weights)][capacity]
       









# weights=[2 , 5, 1 , 3 , 4,8,4]
# values =[15 , 14 ,10 , 45 , 30]
weights=[83,84, 85, 76 ,13 ,87, 2, 23, 33, 82, 79, 100, 88, 85, 91, 78, 83, 44, 4, 50 ,11 ,68 ,90, 88, 73, 83, 46, 16, 7, 35, 76, 31, 40, 49, 65, 2, 18, 47, 55, 38, 75, 58, 86, 77, 96, 94, 82, 92, 10, 86, 54, 49, 65, 44, 77, 22, 81, 52]
values =[57, 95, 13 ,29 ,1 ,99, 34, 77, 61, 23, 24, 70, 73, 88, 33, 61, 43, 5, 41, 63, 8, 67, 20, 72, 98, 59, 46, 58, 64, 94, 97, 70, 46, 81, 42, 7, 1, 52, 20, 54, 81, 3, 73, 78, 81, 11, 41, 45, 18, 94, 24, 82, 9, 19, 59, 48, 2, 72]

capacity= 41
print(knapsack(weights,values,capacity))
