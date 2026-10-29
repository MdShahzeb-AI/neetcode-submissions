class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        el = {}
        for i in nums:
            if i in el:
                el[i] += 1
            else:
                el[i] = 1
        el_s = sorted(el, key=el.get)
        return el_s[-k:]

        