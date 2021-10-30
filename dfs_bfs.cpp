#include <bits/stdc++.h>
using namespace std;
#define ll long long int
#define vi vector<int>
#define vii vector<vector<int>>
#define V 5

    
void print(vector<int> graph[])
{
    for(int i=0; i<V; i++)
    {
        cout<<i;
        for(auto x:graph[i])
            cout<<" -> "<<x;
        
        cout<<"\n";
    }
}


void dfs(vector<int> graph[], int u)
{
    vector<bool> visited(V, false);  
    
    visited[u] = true;
    stack<int> s;
    s.push(u);
    int v, w;
    
    cout<<"DFS Traversal:  ";
    
    while(!s.empty())
    {
        v = s.top();
        s.pop();
        cout<<v<<"  ";
        
        for(int i=0; i<graph[v].size(); i++)
        {
            w = graph[v][i];
            if(!visited[w])
            {
                s.push(w);
            }
            
            visited[w] = true;
        }
    }
    
}


void bfs(vector<int> graph[], int u)
{
    vector<bool> visited(V, false);  
    
    visited[u] = true;
    queue<int> s;
    s.push(u);
    int v, w;
    
    cout<<"DFS Traversal:  ";
    
    while(!s.empty())
    {
        v = s.front();
        s.pop();
        cout<<v<<"  ";
        
        for(int i=0; i<graph[v].size(); i++)
        {
            w = graph[v][i];
            if(!visited[w])
            {
                s.push(w);
            }
            
            visited[w] = true;
        }
    }
    
}


int main() {
   
    vii data {  {1, 2},
            {2, 3},
            {3, 4},
            {4, 0},
            {2, 4},
            {2, 0},
            {1, 0}};
            
    vector<int> graph[V];
    int u, v;
    
    for(int i=0; i<data.size(); i++)
    {
        u = data[i][0];
        v = data[i][1];
        graph[u].push_back(v);
        graph[v].push_back(u);
    }
    
    print(graph);
    
    dfs(graph, 1);
    cout<<"\n\n";
    bfs(graph, 1);
}