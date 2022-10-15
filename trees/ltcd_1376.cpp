//LeetCode - problem 1376

	int numOfMinutes(int n, int headID, vector<int>& manager, vector<int>& time) {
		vector<int> adj[n];
		for(int i=0;i<n;i++){
			if(i!=headID)adj[manager[i]].push_back(i);
		}
		queue<pair<int,int>> q;
		int ans = 0;
		q.push({headID,0});
		while(!q.empty()){
			int cur = q.front().first;
			int t = q.front().second;q.pop();

			for(auto& nxt:adj[cur]){
				ans = max(ans,t+time[cur]);
				q.push({nxt,t+time[cur]});
			}
		}
		return ans;
	}
