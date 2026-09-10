class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2:
            return [0,1]

        table = {}

        for i in range(len(nums)):
            table[nums[i]] = i
        
        for i in range(len(nums)):
            check = target - nums[i]

            if check in table and i != table[check]:
                return[i, table[check]]
