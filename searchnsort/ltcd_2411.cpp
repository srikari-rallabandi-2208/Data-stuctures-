//LeetCode - problem 2411

    vector<int> smallestSubarrays(vector<int>& nums) {
        int sz=nums.size();
        vector<vector<int>>arr(31);
        int j=0;
        for(auto & ele:nums){
            for(int i=0;i<31;i++){
                if((ele>>i)&1)
                    arr[i].push_back(j);
            }
            j++;
        }
        vector<int>suf=nums;
        for(int i=sz-2;i>=0;i--)
            suf[i]=nums[i]|suf[i+1];
        vector<int>ans(sz,0);
        for(int i=0;i<sz;i++){
	    int res=1;
            for(int k=0;k<31;k++){
                if((suf[i]>>k)&1){
                    auto it=lower_bound(begin(arr[k]),end(arr[k]),i);
                    int len=(*it)-i+1;
                    res=max(res,len);
                }
            }
            ans[i]=res;
        }
        return ans;
    }
