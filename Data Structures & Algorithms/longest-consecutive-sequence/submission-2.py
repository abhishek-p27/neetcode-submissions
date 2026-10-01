class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_len = 0 
        for num in num_set: 
            if num - 1 in num_set: 
                continue
            length = 0
            curr = num
            while curr in num_set:
                length += 1
                curr += 1 
            max_len = max(length, max_len)
        return max_len 