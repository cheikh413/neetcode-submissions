class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ls=sorted(s)
        lt=sorted(t)
        return lt==ls

        