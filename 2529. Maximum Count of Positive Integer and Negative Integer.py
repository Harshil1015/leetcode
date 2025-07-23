class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < 0:
                left = mid+1
            else :
                right = mid 
        negative_num = left
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] <= 0:
                left = mid+1
            else :
                right = mid 
        positive_num = len(nums)-left
        return max(positive_num,negative_num)