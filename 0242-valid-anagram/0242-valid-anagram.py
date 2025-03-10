class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        isAnagram = False

        if len(s) != len(t):
            return isAnagram

        sorted_s = ''.join(sorted(s))
        sorted_t = ''.join(sorted(t))

        if sorted_s == sorted_t:
            isAnagram = True

        return isAnagram
        
        