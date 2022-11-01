'''
LeetCode - problem 198
'''

    def rob(self, nums: List[int]) -> int:
        max_2_houses_ago = max_last_house = 0
	for house_value in nums:
            max_2_houses_ago, max_last_house = max_last_house, max(max_2_houses_ago + house_value, max_last_house)
            
        return max_last_house
