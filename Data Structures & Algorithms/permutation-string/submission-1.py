class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1f = {}
        for s in s1:
            s1f[s] = 1 + s1f.get(s,0)
        win = len(s1)
        l = 0
        r = 0
        s2sf = {}
        while (r<len(s2)):
            s2sf[s2[r]] = 1 + s2sf.get(s2[r],0)
            if r - l + 1 == win:
                if s1f == s2sf:
                    return True
                s2sf[s2[l]] -=1
                if s2sf[s2[l]] == 0:
                    s2sf.pop(s2[l])
                l += 1
            r+=1
        return False