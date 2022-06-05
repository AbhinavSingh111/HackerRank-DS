class Solution:
	# @param A : tuple of integers
	# @return an integer
	def trap(self,buildings ):
        self.buildings = buildings
        left_largest = [0]
        right_largest = [0]
        water_trapped = []
        for i in range(len(self.buildings)):
            left_largest.append(max(left_largest[i],self.buildings[i]))
        self.buildings = self.buildings[::-1]
        for j in range(len(self.buildings)):
            right_largest.append(max(right_largest[j],self.buildings[j]))
        left_largest.pop(0)
        right_largest.pop(0)
        right_largest.reverse()
        self.buildings = self.buildings[::-1]
        for i in range(len(self.buildings)):
            water_trapped.append(min(left_largest[i],right_largest[i])-self.buildings[i])
        return sum(water_trapped)
