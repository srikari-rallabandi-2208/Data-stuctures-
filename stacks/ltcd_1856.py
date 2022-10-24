'''
LeetCode - problem 1856
'''

	def maxSumMinProduct(self, nums: List[int]) -> int:
		prefixSum = [0]
		res = 0
		for num in nums:
			prefixSum.append(prefixSum[-1] + num)
		stack = [-1]
		for i, num in enumerate(nums + [0]):
			while len(stack) > 1 and num < nums[stack[-1]]:
				last = stack.pop()
				res = max(res, nums[last] * (prefixSum[i] - prefixSum[stack[-1] + 1]))
			stack.append(i)
		return res % (10 ** 9 + 7)
