class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        el = set()
        for i in nums:
            if i not in el:
                el.add(i)
            else:
                return True
        return False 

        