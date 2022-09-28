//LeetCode - problem 1559

class Solution {
    
    void dfs(int n, int m, int x, int y, vector<vector<char>>& grid, vector<vector<int> > &vis, vector<vector<int> > &dis, int len, int prev_len, char ch, bool &ans){
        if(x < 0 || x >= n || y < 0 || y >= m || grid[x][y] != ch){
            return;
        }
        
        int dx[] = {-1, 1, 0, 0};
        int dy[] = {0, 0, 1, -1};
        
        if(vis[x][y] == 1){
            if(abs(dis[x][y] - prev_len) >= 3){
                ans = true;
            }
            return;
        }
        vis[x][y] = 1;
        dis[x][y] = len;
        
        for(int i = 0; i < 4; i++){
            dfs(n ,m, x + dx[i], y + dy[i], grid, vis, dis, len + 1, dis[x][y], ch, ans);
        }
    }
    
    
public:
    bool containsCycle(vector<vector<char>>& grid) {
        int n = grid.size();
        int m = grid[0].size();
        
        vector<vector<int> > vis(n, vector<int> (m, 0));
        vector<vector<int> > dis(n, vector<int> (m, 0));
        
        bool ans = false;
        
        for(int i = 0; i < n; i++){
            for(int j = 0; j < m; j++){
                if(vis[i][j] == 0){
                    dfs(n ,m, i, j, grid, vis, dis, 1, 1, grid[i][j], ans);
                    if(ans == true){
                        return ans;
                    }
                }
            }
        }
        
        return false;
    }
};
