class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        
        def lowerBound(nums,target):
            lb = -1
            low,high = 0,n-1
            while low<=high:
                mid = (low+high)//2
                if nums[mid] >= target:
                    lb = mid
                    high = mid-1
                else:
                    low = mid+1
            return lb
        
        def upperBound(nums ,target):
            ub = -1
            low,high = 0,n-1
            while low <=high:
                mid = (low+high)//2
                if nums[mid]<=target:
                    ub = mid
                    low = mid+1
                else:
                    high = mid-1
            return ub
        lb = lowerBound(nums,target)
        ub = upperBound(nums,target)
        if lb ==-1 or ub==-1 or nums[lb] != target or nums[ub] != target:
            return [-1,-1]
        return [lb , ub]
            