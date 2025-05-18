# Алгоритм Куна для поиска максимального парасочетания в двудольном графе
def bipartite(graph):
    n = len(graph)
    colors = [-1] * n

    for start in range(n):
        if colors[start] == -1:
            queue = [start]
            colors[start] = 0
            while queue:
                u = queue.pop(0)
                for v in graph[u]:
                    if colors[v] == -1:
                        colors[v] = 1 - colors[u]
                        queue.append(v)
                    elif colors[v] == colors[u]:
                        return False, ([], [])
    set1 = [i for i in range(n) if colors[i] == 0]
    set2 = [i for i in range(n) if colors[i] == 1]
    return True, (set1, set2)

def kuhn(graph):
    n = len(graph)
    match = [-1] * n
    result_pairs = []

    def dfs(v, visited):
        for u in graph[v]:
            if not visited[u]:
                visited[u] = True
                if match[u] == -1 or dfs(match[u], visited):
                    match[u] = v
                    return True
        return False

    is_bipartite, parts = bipartite(graph)

    L = parts[0]
    for v in L:
        visited = [False] * n
        if dfs(v, visited):
            pass
    pairs = []
    for u in range(n):
        v = match[u]
        if v != -1:
            pairs.append((v, u))
    return pairs

# наш граф
G={0:[1,3,7],1:[0],2:[3,5,7],3:[0,2],4:[5],5:[2,4],6:[7],7:[0,2,6]}

is_bipartite, parts = bipartite(G)
L=parts[0] #левая доля
R=parts[1] # правая доля
matching_pairs=kuhn(G) # макс.парасочетание


G_oriented = {node: [] for node in G} # ориентируем граф
matching_set = set(matching_pairs)
for u in G:
    for v in G[u]:
        if (u, v) in matching_set or (v, u) in matching_set:
            if u in R and v in L:
                G_oriented[u].append(v)
            else:
                pass
        else:
            if u in L and v in R:
                G_oriented[u].append(v)

spisok_nasitennih_versin_L=[]
for i in range(len(matching_pairs)):
    a=matching_pairs[i][0]
    b=matching_pairs[i][1]
    spisok_nasitennih_versin_L.append(a)
    spisok_nasitennih_versin_L.append(b)


def dfs_stack(graph, start):
    visited = set()
    stack = [start]
    while stack:
        u = stack.pop()
        if u not in visited:
            visited.add(u)
            for i in range(len(graph[u])):
                stack.append(graph[u][i])
    return visited

vse_posetennie=set()
for i in L:
    if i not in spisok_nasitennih_versin_L:
        f=dfs_stack(G_oriented,i)
        vse_posetennie|=f

l=set(L)
r=set(R)
print((l-vse_posetennie)|(vse_posetennie & r)) # L_ + R+