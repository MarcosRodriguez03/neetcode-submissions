class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        count = 0

        for i in range(len(nums)):
            check = target - nums[i]

            if check in hashMap:
                return [hashMap[check], i ]
            hashMap[nums[i]] = i
            

