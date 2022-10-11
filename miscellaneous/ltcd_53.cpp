//LeetCode - problem 53


    int maxSubArray(vector<int>& nums) {
        int curMax = 0, res = INT_MIN, i;
        for(auto x:nums)
        {
            curMax = curMax>0? (curMax + x):x ;
            if(curMax > res ) res = curMax;
        }
        return res;
    }
