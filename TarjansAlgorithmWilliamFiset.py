def tarjan(graph,node_count):
    id = [0]
    sccCount = [0]

    ids = [-1] * node_count
    low = [-1] * node_count 
    onStack = [False] * node_count 
    stack = []

    for i in range(node_count):
        if ids[i] == -1:
            dfsTarjan(i,stack,onStack,ids,low,id,graph,sccCount)
    return (low,sccCount[0])

def dfsTarjan(at,stack,onStack,ids,low,id,graph,sccCount):
    stack.append(at)
    onStack[at] = True
    ids[at] = low[at] = id[0]
    id[0]+=1 
    
    for to in graph[at]:
        if ids[to] == -1:
            dfsTarjan(to,stack,onStack,ids,low,id,graph,sccCount)
        if onStack[to]: 
            low[at] = min(low[at], low[to])

    if ids[at] == low[at]:  #purpose to see if all the nodes in the cycle were visited and we are back to the low link node
        while stack:
            node = stack.pop()
            onStack[node] = False
            low[node] = ids[at] #use?
            if node == at: break
        sccCount[0]+=1

  
if __name__ == "__main__":
    node_count = 5
    #graph = {0:[1], 1:[2], 2:[0], 3: [4,7], 4:[5], 5: [0,6], 6:[4,2,0], 7: [3,5]}
    #graph = {0: [1, 2], 1: [2], 2:[]}
    graph = {0:[1,4], 1: [2], 2: [3], 3: [0], 4: []}
    strongly_connected = {}

    x, y = tarjan(graph,node_count)
    print("x: ",x)
    for key,value in enumerate(x):
        if value not in strongly_connected:
            strongly_connected[value] = [key]
        else:
            strongly_connected[value].append(key)
    print(strongly_connected)