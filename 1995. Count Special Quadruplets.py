# class Solution:
#     def countQuadruplets(self, nums: List[int]) -> int:
#         from collections import Counter

#         n = len(nums)
#         count = 0
#         diff_counter = Counter()

#         # Fix c from right to left
#         for c in range(n - 2, 1, -1):  # c=2,1
#             # Add nums[d] - nums[c] for all d > c
#             for d in range(c + 1, n):
#                 diff = nums[d] - nums[c]
#                 diff_counter[diff] += 1

#             # For all (a, b) pairs where a < b < c
#             for a in range(c):
#                 for b in range(a + 1, c):
#                     total = nums[a] + nums[b]
#                     count += diff_counter[total]

#         return count
class Solution:
    def countQuadruplets(self, nums: list[int]) -> int:
        cnt = 0
        n = len(nums)
        for a in range(n-3):
            for b in range(a+1, n-2):
                for c in range(b+1, n-1):
                    for d in range(c+1,n):
                        if nums[a] + nums[b] + nums[c] == nums[d]:
                            cnt += 1
        return cnt