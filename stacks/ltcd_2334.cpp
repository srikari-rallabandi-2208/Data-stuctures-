//LeetCode - problem 2334

    int validSubarraySize(vector<int>& nums, int threshold) {
        int n = nums.size();
        stack<int> st;
        for (int i = 0; i <= n; ++i) {
            while (!st.empty() and (i == n or nums[st.top()] > nums[i])) {
                int j = st.top(); st.pop(); 
                int left = st.empty() ? -1 : st.top(); 
                int len = i-left-1;
                double t = threshold*1.0/len*1.0;
                if (nums[j] > t) return len;
            }
            st.push(i);
        }
        return -1;
    }
