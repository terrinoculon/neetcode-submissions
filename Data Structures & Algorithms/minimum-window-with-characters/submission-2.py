class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if  t == "":
            return ""
        tfreq = {}
        for c in t:
            tfreq[c] = 1 + tfreq.get(c,0) 
        l = 0
        r = 0
        window = {}
        have = 0
        need = len(tfreq)
        res = [-1,-1]
        res_length = float('Inf')
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c,0)
            if c in tfreq and window[c]== tfreq[c]:
                have+=1
            while have == need:
                if r-l+1 < res_length:
                    res = [l,r]
                    res_length = r-l+1
                cl = s[l]
                window[cl] -=1
                if cl in tfreq and window[cl] <tfreq.get(cl,0):
                    have-=1
                l+=1
        l,r = res
        return s[l:r+1] if (res_length) != float('Inf') else ""