class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i in range(len(nums)):
            check = target - nums[i]
            if check in hashMap:
                return [hashMap[check],i]
            else:
                hashMap[nums[i]] = i
            
        