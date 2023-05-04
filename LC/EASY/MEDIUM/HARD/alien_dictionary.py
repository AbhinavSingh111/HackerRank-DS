def alienword(words):
    adj = {c:set() for w in words for c in w}
    # print(adj)
    for i in range(len(words)-1):
        w1,w2 = words[i],words[i+1]
        minlen = min(len(w1),len(w2))
        if len(w1)>len(w2) and w1[:minlen]==w2[:minlen]:
            return ""
        for j in range(minlen):
            if w1[j]!=w2[j]:
                adj[w1[j]].add(w2[j])
                break
    # print(adj)
    vis={}
    res = []
    def dfs(c):
        # here we are checking if a node is already been visited and if we are seeing if again then is it a part of the path we are visiting
        # if yes , then we return True that  means we encountered a cyclce , which we should not and hence in the main call we return empty string 
        if c in vis:
            return vis[c]
        vis[c]=True
        for neigh in adj[c]:
            if dfs(neigh):
                return True
        vis[c]=False
        res.append(c)
    for c in adj:
        if dfs(c):
            return ""
    res.reverse()
    return "".join(res)




words=["wrt","wrf","er","ett","rftt"]
print(alienword(words))
