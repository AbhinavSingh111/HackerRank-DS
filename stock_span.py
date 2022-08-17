# Design an algorithm that collects daily price quotes for some stock and returns the span of that stock's price for the current day.

# The span of the stock's price today is defined as the maximum number of consecutive days (starting from today and going backward) for which the stock price was less than or equal to today's price.

# For example, if the price of a stock over the next 7 days were [100,80,60,70,60,75,85], then the stock spans would be [1,1,1,2,1,4,6].

# this question is similar to finding nearest larger to left . all we have to do is count the number of elements in bw , including the element itself.

# leetcode
# class StockSpanner:

#     def __init__(self):
#         self.stock = []
#         self.ind = -1
        

#     def next(self, price: int) -> int:
#         self.ind+=1
       
#         while  self.stock and self.stock[-1][0]<=price :
#             self.stock.pop()
#         ans=0
#         if self.stock:
#             ans = self.ind-self.stock[-1][1]
            
#         else:
#             ans=self.ind+1
            
#         self.stock.append((price,self.ind))
#         return ans


# using index alongside stock value and applying nearest greater to left
def stock_span(prices):
    stock=[]
    vector=[]
    for i in range(len(prices)):
        if len(stock)==0:
            vector.append(-1)
        elif len(stock)!=0 and stock[-1][0]>prices[i]:
            vector.append(stock[-1][1])
        elif len(stock)!=0 and stock[-1][0]<=prices[i]:
            while len(stock)!=0 and stock[-1][0]<=prices[i]:
                stock.pop()
            if len(stock)==0 :
                vector.append(-1)
            else:
                vector.append(stock[-1][1])
        stock.append((prices[i],i))
    for i in range(len(vector)):
        vector[i] = i-vector[i]
    return vector


prices = [100,80,60,70,60,75,85]
print(stock_span(prices))
                
