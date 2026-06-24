class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        for i in range(len(s)):
            maxF = 0
            freq = {}
            for j in range(i, len(s)):
                freq[s[j]] = 1 + freq.get(s[j], 0)
                maxF = max(maxF, freq[s[j]])
                if j-i+1-maxF <=k:
                    res = max(res, j-i+1)
        return res

        