class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1f = [0]*26
        for s in s1:
            s1f[ord(s)-ord('a')] += 1
        win = len(s1)
        l = 0
        r = 0
        s2sf = [0] * 26
        while (r<len(s2)):
            s2sf[ord(s2[r])-ord('a')] += 1
            if r - l + 1 == win:
                if s1f == s2sf:
                    return True
                s2sf[ord(s2[l]) -ord('a')] -=1
                l += 1
            r+=1
        return False