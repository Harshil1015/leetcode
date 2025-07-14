class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        min_sum = float('inf')
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    if nums[i] < nums[j] and nums[k] < nums[j]:
                        triplet_sum= nums[i] + nums[j] + nums[k]
                        min_sum = min(triplet_sum , min_sum)
        return min_sum if min_sum != float('inf') else -1