//LeetCode - problem 685

class Solution {
	int findParent(int x, vector<int> & parent){
		if(parent[x] == x) return x;
		return parent[x] = findParent(parent[x],parent);
	}

	bool Union(int u , int v, vector<int>& parent, vector<int>& rank){
		u = findParent(u,parent);
		v = findParent(v,parent);
		if(u != v){
			if(rank[u] > rank[v]){
				parent[v] = u;
				rank[u]++;
			}else{
				parent[u] = v;
				rank[v]++;
			}
			return false;
		}
		else return true;
	}
public:
	vector<int> findRedundantDirectedConnection(vector<vector<int>>& edges) {
		int n = edges.size();
		vector<int> rank(n+1,0) , parent(n+1) , indegree(n+1,-1);
		for(int i = 1 ; i <= n ; i++) parent[i] = i;

		int bl1 = -1 , bl2 = -1;
		for(int i = 0 ; i < n ; i++){
			if(indegree[edges[i][1]] == -1)
				indegree[edges[i][1]] = i;
			else{
				bl1 = i;
				bl2 = indegree[edges[i][1]];
				break;
			}
		}


		for(int i = 0 ; i < n ; i++){
			if(i == bl1) continue;

			int u = edges[i][0];
			int v = edges[i][1];

			if(Union(u,v,parent,rank)){
				if(bl1 == -1){
					return edges[i];
				}else{
					return edges[bl2];
				}
			}
		}
		return edges[bl1];
	}
};
