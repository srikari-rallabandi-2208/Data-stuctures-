//LeetCode - problem 2420

    vector<int> goodIndices(vector<int>& nums, int k) {
        int n = nums.size();
        
        
        vector<int> ans;
        
        vector<int> front(n, 0); 
        vector<int> back(n, 0);
        
        
        front[0] = 0;
        front[1] = 1;
        for(int i = 2; i < n; i ++) {
            if(nums[i - 1] <= nums[i - 2]) {
                front[i] = 1 + front[i - 1];
            } else {
                front[i] = 1;
            }
        }
        
        back[n - 1] = 0;
        back[n - 2] = 1;
        for(int i = n - 3; i >= 0; i --) {
            if(nums[i + 1] <= nums[i + 2]) {
                back[i] = 1 + back[i + 1];
            } else {
                back[i] = 1;
            }
        }
        
        for(int i = k; i < n - k; i ++) {
            if(min(front[i], back[i]) >= k) ans.push_back(i);   
        }
        
        return ans;
    }
