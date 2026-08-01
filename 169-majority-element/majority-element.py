class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        prefix_map = {}
        for num in nums:
            prefix_map[num] = prefix_map.get(num,0)+1
            if prefix_map[num] > n/2:
                return num 