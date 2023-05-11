787. Cheapest Flights Within K Stops

https://leetcode.com/problems/cheapest-flights-within-k-stops/solutions/3509448/bellmon-ford-python/
  
  class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices=[float("INF")]*n
        prices[src]=0
        for i in range(k+1):
            tempPrices = prices.copy()
            for s,d,p in flights:
                if prices[s]==float("INF"):
                    continue
                if prices[s]+p<tempPrices[d]:
                    tempPrices[d] = prices[s]+p
            prices = tempPrices
        return -1 if prices[dst]==float("INF") else prices[dst]
