class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        el = {}
        for i in nums:
            if i in el:
                el[i] += 1
            else:
                el[i] = 1
        bucket = [[] for _ in range(len(nums)+1)]
        for i in el:
            bucket[el[i]].append(i)
        result = []
        for i in range(len(bucket)-1,0,-1):
            for num in bucket[i]:
                result.append(num)
                if len(result) == k:
                    return result
        return result

        