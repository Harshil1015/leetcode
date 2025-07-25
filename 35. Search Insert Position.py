class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # in this code time complexity is O(n) but wee ned to solve this problem in O(log n)
        # for i in range(len(nums)):
        #     if nums[i] == target:
        #         return i
        #     elif nums[i] > target:
        #         return i
        # return len(nums)
        left = 0
        right = len(nums) -1

        while left <= right :
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else :
                right = mid -1
        return left