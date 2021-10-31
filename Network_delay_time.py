class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, K: int) -> int:
        
        graph = collections.defaultdict(list)
        for u,v,w in times:
            graph[u].append((v,w))
            
        dist = [float('inf')]*(n+1)
        visited = [False]*(n+1)
        dist[K] = 0
        
        pr_queue = [(0, K)]
        heapq.heapify(pr_queue)
        
        
        while(len(pr_queue)>0):
            weight, u = heapq.heappop(pr_queue)
            
            if visited[u]==False:
                for v,w in graph[u]:
                    if (weight+w) < dist[v]:
                        dist[v] = weight +w
                    heapq.heappush(pr_queue, (weight+w, v))

                visited[u]= True
              
            
        mx = 0
        # print(dist)
        for i in range(1, n+1):
            if dist[i]==float('inf'):
                return -1
            else:
                mx = max(mx, dist[i])
                
        return mx