class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) !=len(t):
            return False
        for x in s:
            if x in t:
                if s.count(x)!= t.count(x):
                    return False
            else :
                return False
        return True

        