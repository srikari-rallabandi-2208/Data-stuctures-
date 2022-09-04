//LeetCode - problem 81

 bool search(vector<int>& nums, int target) {
        int i=0;
        int j=0;
        for(i=0;i<nums.size()-1;++i)
        {
            if(nums[i]>nums[i+1])
                break;
        }
        int a=0;  
        int b=i;
        int c=i+1;
        int d=nums.size()-1;
        while(a<=b)
        {
            int mid=a+(b-a)/2;
            if(nums[mid]==target)
                return true;
            if(nums[mid]>target)
            {
                b=mid-1;
            }
            else
                a=mid+1;
        }
         while(c<=d)
        {
            int mid=c+(d-c)/2;
            if(nums[mid]==target)
                return true;
            if(nums[mid]>target)
            {
                d=mid-1;
            }
            else
            c=mid+1;
        }
        return false;
