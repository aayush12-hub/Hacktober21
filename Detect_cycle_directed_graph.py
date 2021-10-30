# Detect cycle in Directed graph

import collections

class solution:
    
    def hasCycle(self):
        n = 4
        lst = [[0,1], [0,2], [1,2], [2, 0], [2,3], [3,3]]
        # lst = [[0,1], [1,2], [2,3]]
        # lst = [[0,1], [2,3], [3,1]]
        
        self.graph = collections.defaultdict(list)
        
        for u,v in lst:
            self.graph[u].append(v)
        
        
        # We made 2 lists, one to mark visited nd other for... whether that node is still involved in that recursion 
        # (bcoz it is involved nd we again reach it, it means graph contains a cycle)
        self.visited = [False]*n
        self.rec_stack = [False]*n
        
        
        # Calling dfs for source node
        for i in range(n):
            if self.visited[i]==False:
                if self.dfs(i):
                    return True
            
        return False
        
        
        
    def dfs(self, i):
        
        self.visited[i] = True
        self.rec_stack[i] = True
        
        for neigh in self.graph[i]:
            if self.visited[neigh] == False:
                if self.dfs(neigh):
                    return True
            
            elif self.rec_stack[neigh]==True:
                return True
                
        self.rec_stack[i] = False
        return False
    
    

s1 = solution()
if(s1.hasCycle()):
    print("Graph contains cycle")
else:
    print("Graph doesn't contain cycle")