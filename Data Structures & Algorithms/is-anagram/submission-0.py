class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        hist_s = {}
        hist_t = {}
        for i in range(len(s)):
            hist_s[s[i]] = hist_s.get(s[i],0) + 1
            hist_t[t[i]] = hist_t.get(t[i],0) + 1
        for key in hist_s.keys():
            if key not in hist_t:
                return False
            if hist_s[key] != hist_t[key]:
                return False
        return True

        