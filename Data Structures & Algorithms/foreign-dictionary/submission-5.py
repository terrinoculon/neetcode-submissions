class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        def extract_edge(w1,w2):
            for c1, c2 in zip(w1, w2):
                if c1!=c2:
                    return c1,c2
            if len(w1)<len(w2):
                return False
            return None
        letters = set("".join(words))
        G = defaultdict(list)
        indegrees = {c:0 for c in letters}
        
        for i in range(len(words)-1):
            if words[i] == words[i+1]:
                continue
            edge = extract_edge(words[i], words[i+1])
            if edge is None:
                return ""
            if not edge:
                continue
            u,v = edge
            G[u].append(v)
            indegrees[v] +=  1

        res = [v for v,ind in indegrees.items() if ind==0]
        q = deque(res)
        print(res,q, indegrees, G)
        while q:
            u = q.popleft()
            for v in G[u]:
                indegrees[v]-=1
                if indegrees[v]==0:
                    q.append(v)
                    res.append(v)
        if len(res)!=len(letters):
            return ""

        return "".join(res)
