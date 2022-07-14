//leetcode problem 55 - jump game

void check(vector<int>& nums , bool &ans ,int inde){
        if(index >= nums.size()){
            return;                                       
        }
        if(index == nums.size()-1){
            ans = true;
            return;
        }

        for(int i=1;i<=nums[index];i++){
            check(nums,ans,index+i);
        }
    }
    bool canJump(vector<int>& nums) {
        bool ans = false;
        check(nums, ans, 0);
        return ans;
    }
