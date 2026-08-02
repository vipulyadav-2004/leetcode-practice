class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prefix_map = {}
        for i , nums in enumerate(nums):
            num2 = target - nums
            if num2 in prefix_map:
                return [i,prefix_map[num2]]
            else:
                prefix_map[nums] = i