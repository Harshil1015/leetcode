class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        count = 0
        pair_sum = {}

        for i in nums1:
            for j in nums2:
                total = i + j
                if total in pair_sum:
                    pair_sum[total] += 1
                else:
                    pair_sum[total] = 1
        
        for k in nums3:
            for l in nums4:
                total2 = -(k + l)
                if total2 in pair_sum:
                    count += pair_sum[total2]
        return count