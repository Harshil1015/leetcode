class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # j=0
        # for i in range(len(nums)):
        #     if nums[i] < k:
        #      j += 1
        # return j thats the noraml approch and in this the time complexity is O(n) but we can solve in O(logn)
        nums.sort()
        left = 0
        right = len(nums)
        while left < right :
            mid = (left + right) // 2
            if nums[mid] < k :
                left = mid + 1
            else :
                right = mid 

        return left