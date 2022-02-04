def topsort(graph):
    n = len(graph)
    v = [False] * n

    ordering = [0] * n
    i = n-1

    for at in range(n):
        if v[at] == False:
            i = dfs(i,at,v,ordering,graph)
            
    return ordering

def dfs(i,at,v,ordering,graph):
    v[at] = True
    edges = graph[at] 
    for edge in edges:
        if v[edge] == False:
          i =  dfs(i,edge,v,ordering,graph)

    ordering[i] = at
    return i - 1

if __name__ == "__main__":
    #graph  = {0: [3], 1: [3], 2: [0, 1], 3: [7, 6], 4: [0, 3, 5], 5: [10,9], 6: [8], 7: [9, 8], 8: [11], 9: [12, 11], 10: [9], 11: [],12: []}
    graph = {1: [0]}

    topsort(graph)
