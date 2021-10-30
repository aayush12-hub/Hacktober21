# Dijisktra implementation without using priority queue

def min_dist(dist, visited):
    minn = float('inf')
    
    for i in range(len(dist)):
        if visited[i]==False and dist[i]<minn:
            minn = dist[i]
            min_ind = i
            
    return min_ind
    
def print_res(dist):
    print("Vertex   Distance from source")
    for i in range(len(dist)):
        print(i, "\t\t", dist[i])

def dijikstra(graph, src):
    dist = [float('inf')]*(len(graph))
    dist[src] = 0
    # heapq.heapify(dist)
    visited = [False]*(len(graph))
    
    
    for i in range(len(graph)):
        u = min_dist(dist, visited)
        
        for v in range(0, len(graph)):
            if visited[v]==False and graph[u][v]>0:
                if dist[u]+graph[u][v]<dist[v]:
                    dist[v] = dist[u] + graph[u][v]
   
        visited[u] = True
        
    print_res(dist)
    
    
    

graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0], 
        [4, 0, 8, 0, 0, 0, 0, 11, 0], 
        [0, 8, 0, 7, 0, 4, 0, 0, 2], 
        [0, 0, 7, 0, 9, 14, 0, 0, 0], 
        [0, 0, 0, 9, 0, 10, 0, 0, 0], 
        [0, 0, 4, 14, 10, 0, 2, 0, 0], 
        [0, 0, 0, 0, 0, 2, 0, 1, 6], 
        [8, 11, 0, 0, 0, 0, 1, 0, 7], 
        [0, 0, 2, 0, 0, 0, 6, 7, 0] 
        ]; 
dijikstra(graph, 0)