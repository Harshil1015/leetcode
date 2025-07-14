class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        # count = 0
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         if nums[j] - nums[i] == diff:
        #             if (nums[j] + diff) in nums:
        #                 count += 1
        # return count
        num_set = set(nums)
        count = 0

        for i in range( len (nums)):
            if (nums[i] + diff) in num_set and (nums[i]+ 2*diff) in num_set:
                count+=1
        return count