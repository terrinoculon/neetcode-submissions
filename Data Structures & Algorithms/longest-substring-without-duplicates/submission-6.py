class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:     
        cur_length = 0
        seen = {}
        l = 0
        r = 0
        while r<len(s):
            if s[r] in seen:
                l = max(seen[s[r]] + 1, l)
            seen[s[r]] = r
            cur_length = max(cur_length, r - l + 1)
            r += 1    
        return cur_length