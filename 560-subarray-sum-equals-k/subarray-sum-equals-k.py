class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        prefix_map = {}
        count = 0
        for i,num in enumerate(nums):
            prefix_sum += num
            if prefix_sum == k :
                count += 1
            if prefix_sum-k in prefix_map:
                count += prefix_map[prefix_sum-k]
            prefix_map[prefix_sum] = prefix_map.get(prefix_sum,0)+1
        return count