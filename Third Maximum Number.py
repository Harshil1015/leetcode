from typing import List

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))  # Remove duplicates
        nums.sort(reverse=True)  # Sort in descending order
        if len(nums) >= 3:
            return nums[2]
        else:
            return nums[0]
