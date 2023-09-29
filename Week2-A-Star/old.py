"""
You can create any other helper funtions.
Do not modify the given functions
"""
def converter(adjmat):
    l = len(adjmat[0])
    adjlist = [[] for x in range(l)]
    for i in range(l):
        for j in range(l):
            if(adjmat[i][j]>0):
                adjlist[i].append(j)#(i,j,adjmat[i][j]) )
    return adjlist

def A_star_Traversal(cost, heuristic, start_point, goals):
    """
    Perform A* Traversal and find the optimal path 
    Args:
        cost: cost matrix (list of floats/int)
        heuristic: heuristics for A* (list of floats/int)
        start_point: Staring node (int)
        goals: Goal states (list of ints)
    Returns:
        path: path to goal state obtained from A*(list of ints)
    """
    path = []
    # TODO
    return path

def dfs(adj_list,start_point,goals):
    stack = [(start_point,[start_point])]
    visited = set()
    while stack:
        print(stack)
        (vertex,path) = stack.pop()
        if vertex not in visited:
            if vertex in goals:
                return path
            visited.add(vertex)
            for i in adj_list[vertex]:
                stack.append((i,path+[i]))

def DFS_Traversal(cost, start_point, goals):
    """
    Perform DFS Traversal and find the optimal path 
        cost: cost matrix (list of floats/int)
        start_point: Staring node (int)
        goals: Goal states (list of ints)
    Returns:
        path: path to goal state obtained from DFS(list of ints)
    """
    
    path = []
    l = len(cost[0])
    adj_list = converter(cost)
    visited = [False]*l
    
    print(dfs(adj_list,start_point,goals))
    return path
