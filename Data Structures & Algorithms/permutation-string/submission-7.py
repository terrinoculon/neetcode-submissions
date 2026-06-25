class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if (len(s1)>len(s2)):
            return False
        s1f = [0]*26
        s2f = [0]*26
        for i in range(len(s1)):
            s1f[ord(s1[i])-ord('a')] += 1
            s2f[ord(s2[i])-ord('a')] +=1
        matches = 0
        for i in range(26):
            if s2f[i] == s1f[i]:
                matches+=1
        l = 0
        for r in range(len(s1),len(s2)):
            if matches == 26:
                return True

            index_r = ord(s2[r]) - ord('a')
            index_l = ord(s2[l])-ord('a')
            s2f[index_l] -=1
            if s2f[index_l] == s1f[index_l]:
                matches +=1
            elif s2f[index_l] == s1f[index_l] - 1:
                matches -=1
            
            s2f[index_r] +=1
            if s2f[index_r] == s1f[index_r]:
                matches +=1
            elif s2f[index_r] == s1f[index_r] + 1:
                matches -=1
            l+=1
        return matches==26
            
