class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        count = 0
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[j] - nums[i] == diff:
                    if (nums[j] + diff) in nums:
                        count += 1
        return count