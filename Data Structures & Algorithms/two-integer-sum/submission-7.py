class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2:
            return [0,1]

        table = {}

        for i in range(len(nums)):
            check = target - nums[i]

            if check in table:
                return[table[check], i]
            table[nums[i]] = i

