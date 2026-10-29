class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_p = [0] * 26
        t_p = [0] * 26
        for i in s:
            s_p[ord(i) - ord('a')] += 1
        for i in t:
            t_p[ord(i) - ord('a')] += 1
        if s_p == t_p:
            return True
        else:
            return False
        