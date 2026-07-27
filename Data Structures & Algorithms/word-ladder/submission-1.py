class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def possible(w1,w2):
            diff = 0
            for c1,c2 in zip(w1,w2):
                if c1!=c2:
                    diff+=1
                if diff>1:
                    return False
            return True
        words = [beginWord] + wordList
        src, goal = 0, None
        G = [[] for _ in range(len(words))]
        for i in range(len(words)):
            if words[i] == endWord:
                goal = i
            for j in range(i+1, len(words)):
                if possible(words[i], words[j]):
                    G[i].append(j)
                    G[j].append(i)
        
        q = deque([(src,1)])
        seen=set()
        while q:
            u, d = q.popleft()
            seen.add(u)
            if u == goal:
                return d
            for v in G[u]:
                if v not in seen:
                    q.append((v, d+1))
        return 0
        