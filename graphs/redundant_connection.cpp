//LeetCode - problem 684

	int FindParent(int node , vector<int>& parent){
		if(parent[node] == node) return node;
		return parent[node] = FindParent(parent[node],parent);
	}

	bool hascycle(int u , int v,  vector<int> &parent){
		int u_parent = FindParent(u,parent);
		int v_parent = FindParent(v,parent);
		return u_parent == v_parent;
	}
public:
	vector<int> findRedundantConnection(vector<vector<int>>& arr) {
		int n = arr.size();
		vector<int> parent(n+1);
		for(int i = 0 ; i <= n ; i++) parent[i] = i;
		int start = -1 , end = -1;
		for(int i = 0 ; i < n ; i++){
			int u = arr[i][0] , v = arr[i][1];
			if(hascycle(u,v,parent)){
				start = u, end = v;
				continue;
			}
			parent[FindParent(v,parent)] = u;
		}
		return {start,end};
	}
