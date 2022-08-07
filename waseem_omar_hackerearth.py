# You are given a grid of size 3*3 that has the following specifications:

# Each cell in the grid is either empty '.' or occupied '*'.
# you can't move to an occupied cell.
# Wesam starts at cell (1,1) and wants to reach Omar who is in cell (3,3).
# Wesam can move vertically, horizontally, and diagonally.
# Note:If Wesam is standing at cell (x,y), he can go to :(x+1,y) , (x-1,y), (x,y+1) , (x,y-1), (x+1,y+1) , (x-1,y-1).

# Note: rows are numbered from top to down, and columns are numbered from left to right.

# Write a program to find if Wesam can reach Omar or not.

# Input format:

# First line: T (number of test cases)
# For each test case
# 3 lines: 3 characters (denoting each cell in the grid.
# It's guaranteed that cell (1,1) and cell (3,3) are empty.
# n= int(input())
# for _ in range(n): 
#     grid=[]
#     for i in range(3):
#         x=input()
#         if len(x)!=3:
#             x=input()
#         grid.append([i for i in x])
#     def does_waseem_reaches_omar(grid):
#         if grid[1][1]=='.': return "YES"
#         if grid[1][0]=='.' and grid[2][1]=='.':return "YES"
#         if grid[0][1]=='.' and grid[1][2]=='.':return "YES"
#         else: return "NO"
#     print(does_waseem_reaches_omar(grid))

def does_waseem_reaches_omar(grid):
    for i in range(len(grid)):
        for j in range(len(grid)):
                if grid[i][j]=="*":
                        break
                if i<2 and j<2:
                    if grid[i+1][j+1]=='.':
                        return "YES"
                    
        return "NO"





grid=[['.','.','.'],['.','*','*'],['.','*','.']]
print(does_waseem_reaches_omar(grid))
