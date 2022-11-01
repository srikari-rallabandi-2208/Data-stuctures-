//LeetCode - problem 198

int rob(vector<int>& nums) {
	int len=nums.size();
	if(0==len) 
		return 0;
	vector<int> bag;
	if(len>0)  
		bag.push_back(nums[0]);
	if(len>1) 
		bag.push_back(max(nums[0],nums[1]));
	for(int i=2;i<len;++i)
		bag.push_back(max(bag[i-1],nums[i]+bag[i-2]));
	return bag[len-1];
}
