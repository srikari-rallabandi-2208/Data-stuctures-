//LeetCode - problem 376

    int wiggleMaxLength(vector<int>& a) {
        
        int n = a.size();
        if(n == 0) return 0;
        
        vector<int> up(n,1), down(n,1);
        for(int i = 1 ; i < n ; i++) {
            up[i] = up[i-1], down[i] = down[i-1];
        	if(a[i] > a[i-1]) up[i] = down[i-1] + 1;
        	if(a[i] < a[i-1]) down[i] = up[i-1] + 1;
        }

    	return max(up[n-1], down[n-1]);
    }
