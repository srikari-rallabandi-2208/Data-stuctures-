//LeetCode - problem 841

    vector<bool>visited;
    
    void dfs(vector<vector<int>>& rooms, int v) {
        
        if (visited[v]) return;
        
        visited[v] = true;
        for (auto it = rooms[v].begin(); it != rooms[v].end(); it++)
            dfs(rooms, *it);
    }
public:
    bool canVisitAllRooms(vector<vector<int>>& rooms) {
        
        int n = rooms.size();
        
        visited.resize(n, false);
        
        dfs(rooms, 0);
        
        for (int i = 0; i < visited.size(); i++) 
            if (!visited[i])
                return false;
        
        return true;
    }
