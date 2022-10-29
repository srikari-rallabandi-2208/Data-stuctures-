//LeetCode - problem 611

    int triangleNumber(vector<int>& nums) {
        int cnt = 0;
        int n = nums.size();
        sort(nums.begin(),nums.end());
        for(int i=2;i<n;i++)
        {
            int l = 0;
            int h = i-1;
            while(l<h)
            {
                if(nums[l]+nums[h] > nums[i])
                {
                    cnt += (h-l);
                    h--;
                }
                else
                {
                    l++;
                }
            }
        }
        return cnt;
    }
