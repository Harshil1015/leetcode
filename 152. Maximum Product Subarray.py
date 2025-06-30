class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product=nums[0]
        curr_max=nums[0]
        curr_min=nums[0]
        for num in nums[1:]:
            temp_max=max(num,curr_max*num,curr_min*num)
            curr_min=min(num,curr_max*num,curr_min*num)
            curr_max=temp_max
            max_product=max(max_product,curr_max)
        return max_product