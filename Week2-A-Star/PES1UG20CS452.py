import logging
"""
You can create any other helper funtions.
Do not modify the given functions
"""
def transformer(adjmat):
    l = len(adjmat[0])
    adjlist = [[] for x in range(l)]
    for i in range(l):
        for j in range(l):
            if(adjmat[i][j]>0):
                adjlist[i].append(j)
    return adjlist


def dfs(adj_list,v,goal,visited,path):
    path+=[v]
    visited[v] = True
    if v in goal:
        for x in range(len(visited)):
            visited[x] = True
    for x in adj_list[v]:
        if visited[x] == False: 
            dfs(adj_list,x,goal,visited,path)


def astar(cost,heuristic,v,goals,visited,path,g):
    path+=[v]
    visited[v] = True
    if v in goals:
        for x in range(len(visited)):
            visited[x] = True
        #visited = [[True] for x in range(len(visited))]
    nextvlist = []
    
    for i in range(len(cost[0])):
        if (cost[v][i] > 0 and visited[i] == False):
            nextvlist += [ (i,cost[v][i],heuristic[i]) ]
    nextvlist = sorted(nextvlist,key = lambda x: x[1]+x[2])
    
    for i in nextvlist:
        if(i[0] in goals):
            astar(cost,heuristic,i[0],goals,visited,path,g)

    if(len(nextvlist) !=0): 
        minm = nextvlist[0][1] + nextvlist[0][2]
        nextvlist = list(filter(lambda x: x[1]+x[2] == minm ,nextvlist))
        for (u,d,h) in reversed(nextvlist):
            if visited[u] == False:
                g+=d 
                astar(cost,heuristic,u,goals,visited,path,g)

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
    visited = [False]*len(cost[0])
    astar(cost,heuristic,start_point,goals,visited,path,0)
    return path




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
    adjacency_list = transformer(cost)
    visited = [False]* len(cost[0])
    dfs(adjacency_list,start_point,goals,visited,path)
    return path
