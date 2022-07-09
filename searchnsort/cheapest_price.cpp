//leetcode problem 787 - cheapest flight within k stops
//this solution is for my reference

int findCheapestPrice(int n, vector<vector<int>>& flights, int src, int dst, int ) {
        vector<pair<int,int>> adj[n];
        int m = flights.size();
        for(int i=0;i<m;i++){
            int p = flights[i][0];
            int q = flights[i][1];
            adj[p].push_back({q,flights[i][2]});
        }
        queue<pair<int,int>>q;
        vector<bool> vis(n,0);
        q.push({0,src});
        vector<int>dist(n,INT_MAX);
        dist[src]=0;
        k+=1; 
        while(!q.empty()){
            int size=q.size();
            k--;
            if(k<0) 
                break;
            for(int i=0;i<size;i++){
                auto p = q.front();
                int node = p.second;
                int wt = p.first;
                q.pop();
                for(auto x:adj[node]){
                    if(x.second+wt<dist[x.first])
                    {
                        dist[x.first]=x.second+wt;
                        q.push({dist[x.first],x.first});
                    }            
                }

            }
        }
        return dist[dst]==INT_MAX?-1:dist[dst];
    }
