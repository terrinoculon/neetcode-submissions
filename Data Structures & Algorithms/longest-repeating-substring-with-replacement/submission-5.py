class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxF = 0
        res = 0
        l = 0
        r = 0
        freq = {}
        while r<len(s):
            freq[s[r]] = 1 + freq.get(s[r],0)
            maxF = max(maxF, freq[s[r]])
            if r-l+1-maxF<=k:
                res = max(res, r-l+1)
            else:
                if s[l] == maxF:
                    maxF-=1
                freq[s[l]] -= 1
                l+=1
            r+=1
        return res
                

        