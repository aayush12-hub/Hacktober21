# Detect cycle in undirected graph

import collections

class solution:
    
    def hasCycle(self):
        n = 4
        # lst = [[0,1], [0,2], [1,2], [2, 0], [2,3], [3,3]]
        # lst = [[0,1], [1,2], [2,3]]
        lst = [[0,1], [2,3], [3,1], [1,2]]
        self.graph = collections.defaultdict(list)
        
        for u,v in lst:
            self.graph[u].append(v)
            self.graph[v].append(u)
            
        
        self.visited = [False]*n
        
        # Calling dfs for source node
        for i in range(n):
            if self.visited[i]==True:
                continue
            
            if self.dfs(i, -1):
                return True
                
        return False
        
        
        
    def dfs(self, i, parent):
        
        self.visited[i] = True
        
        for neigh in self.graph[i]:
            if neigh==parent:
                continue
            
            if self.visited[neigh] == True:
                return True
                
            if self.dfs(neigh, i):
                return True
                
        return False
    
    

s1 = solution()
if(s1.hasCycle()):
    print("Graph contains cycle")
else:
    print("Graph doesn't contain cycle")