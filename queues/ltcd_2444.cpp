 long long countSubarrays(vector<int>& nums, int minK, int maxK) 
    {
        long long last_out = -1;
        long long last_min = -1;
        long long last_max = -1;
        
        long long count    = 0;
        
        for (int i = 0; i < nums.size(); i++)
        {
            if (minK <= nums[i] && nums[i] <= maxK)
            {
                if (nums[i] == minK) last_min = i;
                if (nums[i] == maxK) last_max = i;
                count += max(0LL, min(last_min, last_max) - last_out);
            }
            else last_out = i;
        }

        return count;
    }
