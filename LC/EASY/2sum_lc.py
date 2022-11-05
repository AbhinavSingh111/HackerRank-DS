# https://leetcode.com/problems/two-sum/
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for index , element in enumerate(nums):
            if target-element in dic: #checking if a complementry key value already exist in dic
                return dic[target-element],index , # if yes then return the value of that key (which is an index) and the current index
            dic[element] = index #else store the element as a key and its index as value in dic
