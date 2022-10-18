    int catMouseGame(vector<vector<int>>& graph) {
        int n = graph.size();
        std::vector<std::vector<int>> dp(2,std::vector<int>(n*n,0));
        std::queue<std::vector<int>> q;
        
        for(int i=0; i<n; ++i){
            dp[0][i] = 1;
            dp[1][i] = 1;
            dp[0][n*i] = 1;
            dp[1][n*i] = 1;
            q.push({1,0,i});
        }
        
        for(int i=1; i<n; ++i){
            dp[0][n*i+i] = 2;
            dp[1][n*i+i] = 2;
            q.push({1,i,i});
            q.push({0,i,i});
        }

        while(!q.empty()){
            int s = q.size();
            
            for(int c=0; c<s; ++c){
    
                auto const& v = q.front();
                int k(v[0]), i(v[1]), j(v[2]);

                int w = k==0 ? j: i;
                int& u = k==0 ? j: i;
            
                for(uint d=0; d<graph[w].size(); ++d){
                        
                    u = graph[w][d];
                    if(dp[k^1][n*i+j] ==0){    
                        bool bl(false);
                        if(dp[k][n*v[1]+v[2]]%2!=k){
                            int a(i), b(j);
                            int& x = k==0 ? b: a;
                            for(int e=0; e<graph[u].size(); ++e){
                                x = graph[u][e];
                                if(dp[k][n*a+b]!=dp[k][n*v[1]+v[2]]){
                                    bl = true;
                                    break;
                                }
                            }
                        }
                            
                        if(!bl){ 
                            dp[k^1][n*i+j] = dp[k][n*v[1]+v[2]];
                            if(k^1==0&&i==1&&j==2)
                                return dp[k^1][n*i+j];
                            q.push({k^1,i,j});
                        } 
                    }
                }
                q.pop();
            }
        }
        
        return 0;
        
    }
