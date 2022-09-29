//LeetCode - problem 239

   vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        int sum = 0;
        priority_queue<pair<int, int>> heap;
	   for(int i = 0; i < k-1;i++){
            heap.push({nums[i], i + k - 1});
        }
        vector<int> ans;
        for(int i = k-1;i < nums.size();i++){
            heap.push({nums[i], i + k - 1});
            while(heap.top().second < i){
                heap.pop();
            }
            ans.push_back(heap.top().first);
        }
        return ans;
    }
