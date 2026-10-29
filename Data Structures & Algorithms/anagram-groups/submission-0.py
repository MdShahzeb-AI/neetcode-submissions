class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        el = {}
        for i in strs:
            if "".join(sorted(i)) in el:
                el["".join(sorted(i))].append(i)
            else:
                el["".join(sorted(i))] = [i]
        return list(el.values())
        
        