class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:     
        curLength = 0        
        l = 0
        r = 0
        seen = {}
        while r < len(s) : 
            if s[r] in seen: 
                l = max(seen[s[r]] + 1,l)                 
            seen[s[r]] = r 
            curLength =max(curLength, r - l + 1)
            r += 1 
            
        return curLength