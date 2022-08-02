def costOfMinPathInMaze(maze):
    m=len(maze)  #rows
    n=len(maze[0])  #columns
    dp=[[0 for i in range(n)]for i in range(m)]
    for i in range(len(dp)-1,-1,-1):
        for j in range(len(dp[0])-1, -1 ,-1):
            if i==len(dp)-1 and j==len(dp[0])-1:
                dp[i][j]=maze[i][j]
            elif i==len(dp)-1:
                dp[i][j]=dp[i][j+1]+maze[i][j]
            elif j==len(dp[0])-1:
                dp[i][j]=dp[i+1][j]+maze[i][j]
            else:
                dp[i][j]=min(dp[i+1][j],dp[i][j+1])+maze[i][j]
    return dp[0][0]



maze=[[2,8,4,1,6,4,2],[6,0,9,5,3,8,5],[1,4,3,4,0,6,5],
[6,4,7,2,4,6,1],[1,0,3,7,1,2,7],[1,5,3,2,3,0,9],[2,2,5,1,9,8,2]]
# maze=[[3,1],[4,3]]
# maze=[[1,2,3],[4,5,6]]
print(costOfMinPathInMaze(maze))
