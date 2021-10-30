#include <bits/stdc++.h>
using namespace std;
#define ll long long int
#define vi vector<int>
#define vii vector<vector<int>>

int main() {
   
    vii data {  {1, 2},
            {2, 3},
            {3, 4},
            {4, 0},
            {2, 4},
            {2, 0},
            {1, 0}};
            
    vector<int> graph[5];
    int u, v;
    
    for(int i=0; i<data.size(); i++)
    {
        u = data[i][0];
        v = data[i][1];
        graph[u].push_back(v);
        graph[v].push_back(u);
    }
    
    for(int i=0; i<5; i++)
    {
        cout<<i;
        for(auto x:graph[i])
            cout<<" -> "<<x;
        
        cout<<"\n";
    }
    
    
}