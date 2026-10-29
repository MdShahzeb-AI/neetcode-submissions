class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        el = {}
        for i in range(len(nums)):
            if (target - nums[i]) in el:
                return [el[target - nums[i]],i]
            else:
                el[nums[i]] = i


        