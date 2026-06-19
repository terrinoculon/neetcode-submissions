class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        hist = {}
        for i in range(len(s)):
            hist[s[i]] = hist.get(s[i], 0) + 1
            hist[t[i]] = hist.get(t[i], 0) - 1        
        
        return all(val == 0 for val in hist.values())


        