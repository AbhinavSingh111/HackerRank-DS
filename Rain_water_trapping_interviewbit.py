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

###

class Solution:
    def trap(self, height: List[int]) -> int:
        left_largest = []
        right_largest = []

        for i in range(len(height)):
            if i==0:
                left_largest.append(height[i])
            else:
                left_largest.append(max(left_largest[-1],height[i]))


        for i in range(len(height)-1,-1,-1):
            if i==len(height)-1:
                right_largest.append(height[-1])
            else:
                right_largest.append(max(right_largest[-1],height[i]))
        right_largest = right_largest[::-1]


        water = 0
        for i in range(len(height)):
            water+=(min(left_largest[i],right_largest[i])-height[i])
        return water
