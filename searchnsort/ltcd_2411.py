'''
LeetCode - problem 2441
'''

    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        maximum_bits = int(log(10**9, 2)) + 1
        index_for_each_bit = [[] for _ in range(maximum_bits)]
        for i in range(len(nums)):
            n = nums[i]
            for bit in range(maximum_bits):
                if n % 2 == 1:
                    index_for_each_bit[bit].append(i)
                n >>= 1

        res = []
        for i in range(len(nums)):
            cur_idx = [i]
            n = nums[i]
            for bit in range(maximum_bits):
                bit_index = index_for_each_bit[bit]
                if n % 2 == 0:
                    k = bisect_left(bit_index, i)
                    if k < len(bit_index):
                       cur_idx.append(bit_index[k])
                n >>= 1
            res.append(max(cur_idx) - i + 1)
        return res
